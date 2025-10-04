# server_qt_gui.py
import sys, os, threading, logging, traceback
from pathlib import Path
from typing import Dict, Any, List

from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTabWidget, QFormLayout, QLineEdit,
    QVBoxLayout, QPushButton, QTextEdit, QListWidget, QListWidgetItem,
    QHBoxLayout, QMessageBox, QInputDialog, QFileDialog, QLabel, QSplitter
)

# ---- optional dark theme -----------------------------------------------------
try:
    import qdarktheme
except Exception:
    qdarktheme = None

# ---- project imports ---------------------------------------------------------
from server import Server  # required

# Optional pieces (we'll guard usage with runtime checks)
Simulation = None
SimulationSaver = None
ModManager = None

try:
    # Adjust these imports to your actual package layout if needed
    from simulation import Simulation as _Simulation
    Simulation = _Simulation
except Exception:
    pass

try:
    from simulation_saver import SimulationSaver as _SimulationSaver
    SimulationSaver = _SimulationSaver
except Exception:
    pass

try:
    # If your ModManager lives elsewhere, just tweak this import
    from simantics_common.mod_manager import ModManager as _ModManager
    ModManager = _ModManager
except Exception:
    pass


# ---- logging to Qt bridge ----------------------------------------------------
class QtLogBridge(QObject):
    append = Signal(str)

class QtLogHandler(logging.Handler):
    def __init__(self, bridge: QtLogBridge):
        super().__init__()
        self.bridge = bridge

    def emit(self, record):
        try:
            msg = self.format(record)
            self.bridge.append.emit(msg)
        except Exception:
            # never raise from logging
            pass


# ---- main window -------------------------------------------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SimAntics Server (Qt)")
        self.resize(1100, 750)

        # runtime state
        self.server_running: bool = False
        self.simulation = None
        self.server: Server | None = None
        self.sim_thread: threading.Thread | None = None
        self.srv_thread: threading.Thread | None = None
        self.load_from_save: bool = False

        # initial configs (update at New/Load)
        self.simulation_config: Dict[str, Any] = {
            "save_name": "",
            "x": 10,
            "y": 10,
            "map_update_interval": 1.0,
            "gas_update_interval": 1.0,
            "max_player_gas_count": 32,
        }
        self.server_config: Dict[str, Any] = {
            "port": 65432,
            "udp_port": 65433,
            "inactivity_timeout": 15,
            "message_interval_rate": 5,
        }

        # UI
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.config_tab = QWidget()
        self.run_tab = QWidget()
        self.tabs.addTab(self.config_tab, "Config")
        self.tabs.addTab(self.run_tab, "Run")

        self.sim_inputs: Dict[str, QLineEdit] = {}
        self.srv_inputs: Dict[str, QLineEdit] = {}

        self._build_config_tab()
        self._build_run_tab()
        self._attach_logger()

        # populate mods list (best effort)
        self._load_mods_safe()

    # ---------- UI builders ----------
    def _build_config_tab(self):
        root = QVBoxLayout(self.config_tab)

        # Forms in a splitter so it resizes nicely vs lists
        left_forms = QWidget()
        vf = QVBoxLayout(left_forms)

        # Simulation fields
        sim_form = QFormLayout()
        for k in self.simulation_config:
            w = QLineEdit(str(self.simulation_config[k]))
            self.sim_inputs[k] = w
            sim_form.addRow(k, w)

        # Server fields
        srv_form = QFormLayout()
        for k in self.server_config:
            w = QLineEdit(str(self.server_config[k]))
            self.srv_inputs[k] = w
            srv_form.addRow(k, w)

        vf.addWidget(QLabel("Simulation"))
        vf.addLayout(sim_form)
        vf.addSpacing(8)
        vf.addWidget(QLabel("Server"))
        vf.addLayout(srv_form)
        vf.addStretch(1)

        # Mods lists
        right_lists = QWidget()
        hl = QVBoxLayout(right_lists)

        lists_row = QHBoxLayout()
        self.inactive_list = QListWidget()
        self.active_list = QListWidget()


        lists_row.addWidget(self.inactive_list)
        lists_row.addWidget(self.active_list)

        hint = QLabel("Double-click to move mods ←→")
        hint.setStyleSheet("color: gray;")
        hl.addWidget(hint)
        hl.addLayout(lists_row)

        # Top-level splitter
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_forms)
        splitter.addWidget(right_lists)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)
        root.addWidget(splitter)

        # Buttons
        btn_row = QHBoxLayout()
        self.btn_new_game = QPushButton("New Game")
        self.btn_load_save = QPushButton("Load Save")
        self.btn_pick_save_dir = QPushButton("Browse Saves…")
        btn_row.addWidget(self.btn_new_game)
        btn_row.addWidget(self.btn_load_save)
        btn_row.addStretch(1)
        btn_row.addWidget(self.btn_pick_save_dir)
        root.addLayout(btn_row)

        # wiring
        self.inactive_list.itemDoubleClicked.connect(self._activate_mod)
        self.active_list.itemDoubleClicked.connect(self._deactivate_mod)
        self.btn_new_game.clicked.connect(self._new_game_dialog)
        self.btn_load_save.clicked.connect(self._load_save_dialog)
        self.btn_pick_save_dir.clicked.connect(self._browse_saves)

    def _build_run_tab(self):
        root = QVBoxLayout(self.run_tab)

        # Controls
        btn_row = QHBoxLayout()
        self.btn_run = QPushButton("Run Server")
        self.btn_save = QPushButton("Save Simulation")
        self.btn_save.setEnabled(False)

        btn_row.addWidget(self.btn_run)
        btn_row.addWidget(self.btn_save)
        btn_row.addStretch(1)

        root.addLayout(btn_row)

        # Log viewer
        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)
        root.addWidget(self.log_view, 1)

        # wire
        self.btn_run.clicked.connect(self._toggle_server)
        self.btn_save.clicked.connect(self._save_simulation)

    def _attach_logger(self):
        # configure root logger if not already
        if not logging.getLogger().handlers:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            )

        self.log_bridge = QtLogBridge()
        self.log_bridge.append.connect(self._append_log)
        self.qt_handler = QtLogHandler(self.log_bridge)
        self.qt_handler.setLevel(logging.INFO)
        self.qt_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

        # attach to root so everything funnels in
        logging.getLogger().addHandler(self.qt_handler)

    def _append_log(self, s: str):
        self.log_view.append(s)

    # ---------- Config helpers ----------
    def _refresh_fields(self):
        for k, w in self.sim_inputs.items():
            w.setText(str(self.simulation_config.get(k, "")))
        for k, w in self.srv_inputs.items():
            w.setText(str(self.server_config.get(k, "")))

    def _enable_config_fields(self, enable: bool):
        for w in list(self.sim_inputs.values()) + list(self.srv_inputs.values()):
            w.setEnabled(enable)
        self.inactive_list.setEnabled(enable)
        self.active_list.setEnabled(enable)
        self.btn_new_game.setEnabled(enable)
        self.btn_load_save.setEnabled(enable)
        self.btn_pick_save_dir.setEnabled(enable)

    def _coerce_inputs_into_dicts(self):
        def _coerce(dst: Dict[str, Any], inputs: Dict[str, QLineEdit]):
            for k, w in inputs.items():
                text = w.text()
                old = dst.get(k)
                if isinstance(old, int):
                    try:
                        dst[k] = int(text)
                    except Exception:
                        pass
                elif isinstance(old, float):
                    try:
                        dst[k] = float(text)
                    except Exception:
                        pass
                else:
                    dst[k] = text
        _coerce(self.simulation_config, self.sim_inputs)
        _coerce(self.server_config, self.srv_inputs)

    # ---------- Mods ----------
    def _fill_mod_lists(self, active: List[str], inactive: List[str]):
        self.active_list.clear()
        self.inactive_list.clear()
        for name in sorted(inactive):
            self.inactive_list.addItem(QListWidgetItem(name))
        for name in sorted(active):
            self.active_list.addItem(QListWidgetItem(name))

    def _activate_mod(self, item: QListWidgetItem):
        self.active_list.addItem(QListWidgetItem(item.text()))
        self.inactive_list.takeItem(self.inactive_list.row(item))

    def _deactivate_mod(self, item: QListWidgetItem):
        self.inactive_list.addItem(QListWidgetItem(item.text()))
        self.active_list.takeItem(self.active_list.row(item))

    def _load_mods_safe(self):
        """Try to load mods from ModManager; fallback to simple folder scan."""
        try:
            if ModManager is None:
                raise RuntimeError("ModManager not available")
            save_name = self.simulation_config.get("save_name", "") or ""
            mods_config = None
            try:
                mods_config = ModManager.load_mod_config(save_name)
            except Exception:
                mods_config = None
            available = ModManager.scan_mods_folder()
            # Expecting something like names list; if objects, map to names
            avail_names = [m["name"] if isinstance(m, dict) and "name" in m else str(m) for m in available]
            if hasattr(ModManager, "get_mod_status"):
                active, inactive = ModManager.get_mod_status(mods_config, avail_names)
            else:
                # naive: no active set yet
                active, inactive = [], avail_names
            self._fill_mod_lists([str(a) for a in active], [str(i) for i in inactive])
        except Exception:
            # fallback: list folders under ./mods
            mods_dir = Path("mods")
            if mods_dir.is_dir():
                names = sorted(p.name for p in mods_dir.iterdir() if p.is_dir())
                self._fill_mod_lists([], names)
            else:
                self._fill_mod_lists([], [])

    # ---------- Save folder helpers ----------
    def _browse_saves(self):
        path = QFileDialog.getExistingDirectory(self, "Select saves directory", str(Path.cwd()))
        if path:
            # optional: remember somewhere; for now we just hint user
            QMessageBox.information(self, "Saves", f"Selected: {path}")

    def _enumerate_saves(self) -> List[str]:
        # if your project uses another location, adjust here
        base = Path("saves")
        if not base.exists():
            return []
        return sorted([p.name for p in base.iterdir() if p.is_dir()])

    # ---------- New/Load ----------
    def _new_game_dialog(self):
        name, ok = QInputDialog.getText(self, "New Game", "Enter save name:")
        if not ok or not name:
            return

        # sensible defaults; tweak to your taste
        self.simulation_config.update({
            "save_name": name,
            "x": 10,
            "y": 10,
            "map_update_interval": 1.0,
            "gas_update_interval": 1.0,
            "max_player_gas_count": 32,
        })
        self.server_config.update({
            "port": 65432,
            "udp_port": 65433,
            "inactivity_timeout": 15,
            "message_interval_rate": 5,
        })
        self.load_from_save = False
        self._refresh_fields()
        self._load_mods_safe()

    def _load_save_dialog(self):
        if SimulationSaver is None:
            QMessageBox.critical(self, "Missing component",
                                 "SimulationSaver module not found; cannot load saves.")
            return

        saves = self._enumerate_saves()
        if not saves:
            QMessageBox.information(self, "Load Save", "No save folders found under ./saves")
            return

        choice, ok = QInputDialog.getItem(self, "Load Save", "Choose save:", saves, 0, False)
        if not ok:
            return

        try:
            sim_cfg, srv_cfg = SimulationSaver.get_simulation_config(choice)
            if isinstance(sim_cfg, dict):
                self.simulation_config.update(sim_cfg)
            else:
                self.simulation_config["save_name"] = choice
            if isinstance(srv_cfg, dict):
                self.server_config.update(srv_cfg)
            self.load_from_save = True
            self._refresh_fields()
            self._load_mods_safe()
        except Exception as e:
            QMessageBox.critical(self, "Load Save failed", f"{e}\n\n{traceback.format_exc()}")

    # ---------- Start/Stop ----------
    def _toggle_server(self):
        if not self.server_running:
            self._start_server()
        else:
            self._stop_server()

    def _collect_active_mods(self) -> List[str]:
        return [self.active_list.item(i).text() for i in range(self.active_list.count())]

    def _validate_mods_present(self, chosen: List[str]) -> bool:
        # re-scan available quickly
        available = set()
        try:
            if ModManager is not None:
                available = set([
                    (m["name"] if isinstance(m, dict) and "name" in m else str(m))
                    for m in ModManager.scan_mods_folder()
                ])
            else:
                mods_dir = Path("mods")
                if mods_dir.is_dir():
                    available = set(p.name for p in mods_dir.iterdir() if p.is_dir())
        except Exception:
            pass
        missing = [m for m in chosen if m not in available]
        if missing:
            msg = "The following mods are missing:\n\n" + "\n".join(missing) + "\n\nProceed anyway?"
            ret = QMessageBox.question(self, "Missing Mods", msg,
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            return ret == QMessageBox.Yes
        return True

    def _start_server(self):
        # sanity checks
        if Simulation is None:
            QMessageBox.critical(self, "Missing component",
                                 "Simulation module not found; cannot start server.")
            return

        self._coerce_inputs_into_dicts()
        chosen_mods = self._collect_active_mods()
        if not self._validate_mods_present(chosen_mods):
            return

        # disable UI while running
        self._enable_config_fields(False)
        self.btn_run.setEnabled(False)
        self.btn_run.setText("Starting…")
        QApplication.processEvents()

        try:
            # Build Simulation and Server
            self.simulation = Simulation(
                simulation_config=self.simulation_config,
                mods=chosen_mods,
                load_from_save=self.load_from_save
            )
        except TypeError:
            # If your Simulation has a different signature, show a helpful message
            self._enable_config_fields(True)
            self.btn_run.setEnabled(True)
            self.btn_run.setText("Run Server")
            QMessageBox.critical(self, "Simulation init failed",
                                 "Simulation constructor signature seems different than expected.\n"
                                 "Expected: Simulation(simulation_config=dict, mods=list, load_from_save=bool)")
            return
        except Exception as e:
            self._enable_config_fields(True)
            self.btn_run.setEnabled(True)
            self.btn_run.setText("Run Server")
            QMessageBox.critical(self, "Simulation init failed", f"{e}\n\n{traceback.format_exc()}")
            return

        try:
            self.server = Server(
                simulation=self.simulation,
                host="127.0.0.1",
                port=self.server_config["port"],
                udp_port=self.server_config["udp_port"],
                inactivity_timeout=self.server_config["inactivity_timeout"],
                message_interval_rate=self.server_config["message_interval_rate"],
            )
            # If your Simulation expects to know its server:
            if hasattr(self.simulation, "set_server"):
                try:
                    self.simulation.set_server(self.server)
                except Exception:
                    pass
        except Exception as e:
            self._enable_config_fields(True)
            self.btn_run.setEnabled(True)
            self.btn_run.setText("Run Server")
            QMessageBox.critical(self, "Server init failed", f"{e}\n\n{traceback.format_exc()}")
            return

        # start background threads
        try:
            self.sim_thread = threading.Thread(
                target=self.simulation.start,
                args=[getattr(self.server, "outbound_queue", None)],
                daemon=True
            )
            self.sim_thread.start()
        except Exception as e:
            self._enable_config_fields(True)
            self.btn_run.setEnabled(True)
            self.btn_run.setText("Run Server")
            QMessageBox.critical(self, "Simulation start failed", f"{e}\n\n{traceback.format_exc()}")
            return

        try:
            self.srv_thread = threading.Thread(target=self.server.run, daemon=True)
            self.srv_thread.start()
        except Exception as e:
            # try to stop simulation if server failed to start
            try:
                if hasattr(self.simulation, "stop"):
                    self.simulation.stop()
            except Exception:
                pass
            self._enable_config_fields(True)
            self.btn_run.setEnabled(True)
            self.btn_run.setText("Run Server")
            QMessageBox.critical(self, "Server start failed", f"{e}\n\n{traceback.format_exc()}")
            return

        self.server_running = True
        self.btn_run.setText("Stop Server")
        self.btn_run.setEnabled(True)
        self.btn_save.setEnabled(True)
        self.tabs.setCurrentWidget(self.run_tab)

    def _stop_server(self):
        self.btn_run.setEnabled(False)
        self.btn_run.setText("Stopping…")
        QApplication.processEvents()
        try:
            if self.simulation and hasattr(self.simulation, "stop"):
                self.simulation.stop()
        except Exception:
            pass
        try:
            if self.server and hasattr(self.server, "stop"):
                self.server.stop()
        except Exception:
            pass

        self.server_running = False
        self.btn_run.setText("Run Server")
        self.btn_run.setEnabled(True)
        self.btn_save.setEnabled(False)
        self._enable_config_fields(True)

    # ---------- Save ----------
    def _save_simulation(self):
        if SimulationSaver is None:
            QMessageBox.critical(self, "Missing component",
                                 "SimulationSaver module not found; cannot save.")
            return
        try:
            # sync the name in case user edited it
            self.simulation_config["save_name"] = self.sim_inputs["save_name"].text()
            if not self.simulation:
                QMessageBox.information(self, "Save", "Simulation is not running.")
                return
            SimulationSaver.save_simulation(self.simulation)
            self.log_view.append(f"Saved simulation: {self.simulation_config['save_name']}")
        except Exception as e:
            QMessageBox.critical(self, "Save failed", f"{e}\n\n{traceback.format_exc()}")

    # ---------- window close ----------
    def closeEvent(self, e):
        try:
            if self.server_running:
                if self.simulation and hasattr(self.simulation, "stop"):
                    self.simulation.stop()
                if self.server and hasattr(self.server, "stop"):
                    self.server.stop()
        finally:
            e.accept()


# ---- main entry --------------------------------------------------------------
def main():
    app = QApplication(sys.argv)
    if qdarktheme:
        try:
            qdarktheme.setup_theme("dark")
        except Exception:
            pass
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

