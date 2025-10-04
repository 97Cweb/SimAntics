# client_qt_gui.py
import sys, os, io, json5, time, base64, zipfile, shutil, threading, traceback
from pathlib import Path
from typing import Optional, Tuple

from PySide6.QtCore import Qt, QTimer, Signal, QObject, QUrl
from PySide6.QtGui import QAction, QFont, QDesktopServices, QPainter
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDockWidget, QFileSystemModel, QTreeView,
    QPlainTextEdit, QTextEdit, QLineEdit, QPushButton, QLabel, QToolBar, QStatusBar,
    QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox, QFileDialog, QGraphicsView,
    QGraphicsScene, QGraphicsPixmapItem, QDialog, QDialogButtonBox, QStackedWidget
)

# ---- Optional dark theme -----------------------------------------------------
try:
    import qdarktheme
except Exception:
    qdarktheme = None

# ---- Optional Steamworks -----------------------------------------------------
STEAM = None
try:
    from steamworks import STEAMWORKS
    STEAM = STEAMWORKS()
    STEAM.initialize()
except Exception:
    STEAM = None  # We'll allow manual username entry

# ---- Project imports (unchanged) --------------------------------------------
from network_manager import NetworkManager


# --------------------------- Game Canvas -------------------------------------
class GameCanvas(QGraphicsView):
    """Simple placeholder canvas. Replace with your real renderer."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene_ = QGraphicsScene(self)
        self.setScene(self.scene_)
        self.setRenderHints(self.renderHints() | QPainter.RenderHint.Antialiasing | QPainter.RenderHint.SmoothPixmapTransform)
        self.setSceneRect(0, 0, 1024, 640)

        pm = self._square_pixmap(28)
        self.sprite = QGraphicsPixmapItem(pm)
        self.scene_.addItem(self.sprite)
        self.sprite.setPos(8, 8)
        self.dx, self.dy = 2.0, 1.3

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._tick)
        self.timer.start(16)  # ~60 fps

    def _square_pixmap(self, size: int):
        from PySide6.QtGui import QPixmap, QPainter, QColor
        pm = QPixmap(size, size); pm.fill(Qt.transparent)
        p = QPainter(pm)
        p.fillRect(0, 0, size, size, QColor("#49a6ff"))
        p.end()
        return pm

    def _tick(self):
        rect = self.sceneRect()
        x = self.sprite.x() + self.dx
        y = self.sprite.y() + self.dy
        if x < 0 or x > rect.width() - 28: self.dx *= -1
        if y < 0 or y > rect.height() - 28: self.dy *= -1
        self.sprite.setPos(x, y)


# --------------------------- Signals Bridge ----------------------------------
class GuiBus(QObject):
    log = Signal(str)
    tcp_message = Signal(dict)      # parsed JSON
    udp_state = Signal(dict)        # parsed JSON state (e.g., frame updates)
    connected = Signal(str)         # server_id
    disconnected = Signal()


# --------------------------- Login Dialog ------------------------------------
class LoginDialog(QDialog):
    """Popup login form — returns connection params on accept()."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Join Server")
        self.setModal(True)
        layout = QVBoxLayout(self)

        form = QFormLayout()
        self.host = QLineEdit("127.0.0.1")
        self.tcp = QLineEdit("65432")
        self.udp = QLineEdit("65433")
        self.user = QLineEdit()
        self.passw = QLineEdit(); self.passw.setEchoMode(QLineEdit.Password)
        self.keepalive = QLineEdit("5")

        if STEAM:
            try:
                sid = STEAM.Users.GetSteamID()
                self.user.setText(str(sid))
                self.user.setReadOnly(True)
            except Exception:
                pass

        form.addRow("Host", self.host)
        form.addRow("TCP Port", self.tcp)
        form.addRow("UDP Port", self.udp)
        form.addRow("Username", self.user)
        form.addRow("Password", self.passw)
        form.addRow("Keep-Alive (s)", self.keepalive)

        layout.addLayout(form)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self._validate_and_accept)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)

    def _validate_and_accept(self):
        try:
            int(self.tcp.text() or "0")
            int(self.udp.text() or "0")
            float(self.keepalive.text() or "0")
        except ValueError:
            QMessageBox.critical(self, "Invalid Input", "Please enter valid numeric values for ports and keep-alive.")
            return
        if not self.user.text().strip():
            QMessageBox.critical(self, "Invalid Input", "Username is required.")
            return
        self.accept()

    def params(self) -> Tuple[str, int, int, str, str, int]:
        return (
            self.host.text().strip(),
            int(self.tcp.text()),
            int(self.udp.text()),
            self.user.text().strip(),
            self.passw.text(),
            int(float(self.keepalive.text()))
        )


# --------------------------- Main Menu Screen --------------------------------
class MainMenu(QWidget):
    join_clicked = Signal()
    quit_clicked = Signal()

    def __init__(self):
        super().__init__()
        v = QVBoxLayout(self)
        v.addStretch(1)
        title = QLabel("SimAntics")
        font = title.font(); font.setPointSize(24); font.setBold(True); title.setFont(font)
        title.setAlignment(Qt.AlignHCenter)
        v.addWidget(title)

        v.addSpacing(16)
        btn_join = QPushButton("Join")
        btn_join.setFixedWidth(200)
        btn_join.clicked.connect(self.join_clicked.emit)
        btn_quit = QPushButton("Quit")
        btn_quit.setFixedWidth(200)
        btn_quit.clicked.connect(self.quit_clicked.emit)

        hv = QHBoxLayout()
        hv.addStretch(1); hv.addWidget(btn_join); hv.addSpacing(16); hv.addWidget(btn_quit); hv.addStretch(1)
        v.addLayout(hv)
        v.addStretch(2)


# --------------------------- Game Screen (docks) -----------------------------
class GameScreen(QWidget):
    """Holds the canvas and all docks/toolbars. Exposes connect/disconnect APIs."""
    def __init__(self, bus: GuiBus):
        super().__init__()
        self.bus = bus
        self.network: Optional[NetworkManager] = None
        self.keep_alive_thread: Optional[threading.Thread] = None
        self.udp_thread: Optional[threading.Thread] = None
        self.tcp_thread: Optional[threading.Thread] = None
        self.running = False
        self.last_frame = 0
        self.server_id: Optional[str] = None
        self.save_dir: Optional[Path] = None
        self._opened_path: Optional[Path] = None

        # Layout: we embed into a QMainWindow-like container to allow docks
        self._root = QMainWindow()
        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self._root)

        # central canvas
        self.canvas = GameCanvas()
        self._root.setCentralWidget(self.canvas)

        # docks
        self._build_logs_dock()
        self._build_editor_dock()
        self._build_files_dock()

        # top toolbar: in-game actions (no connect fields here)
        self._build_toolbar()
        self._root.setStatusBar(QStatusBar(self._root))

        # bus wiring
        self.bus.log.connect(self._append_log)
        self.bus.tcp_message.connect(self._on_tcp_json)
        self.bus.udp_state.connect(self._on_udp_state)
        self.bus.connected.connect(self._on_connected)
        self.bus.disconnected.connect(self._on_disconnected)

    # -------------- UI pieces --------------
    def _build_toolbar(self):
        tb = QToolBar("Game")
        self._root.addToolBar(tb)

        self.act_disconnect = QAction("Disconnect", self)
        self.act_disconnect.triggered.connect(self.disconnect_from_server)
        tb.addAction(self.act_disconnect)

        tb.addSeparator()
        self.btn_upload = QPushButton("Upload Save Folder")
        self.btn_upload.setEnabled(False)
        self.btn_upload.clicked.connect(self._upload_save_folder)
        tb.addWidget(self.btn_upload)

        self.btn_open_save = QPushButton("Open Save Dir…")
        self.btn_open_save.setEnabled(False)
        self.btn_open_save.clicked.connect(self._open_save_dir)
        tb.addWidget(self.btn_open_save)

        tb.addSeparator()
        act_open = QAction("Open File…", self); act_open.triggered.connect(self._editor_open)
        act_save = QAction("Save File", self); act_save.triggered.connect(self._editor_save)
        tb.addAction(act_open); tb.addAction(act_save)

    def _build_logs_dock(self):
        self.log_view = QTextEdit(); self.log_view.setReadOnly(True)
        dock = QDockWidget("Logs")
        dock.setWidget(self.log_view)
        dock.setObjectName("LogsDock")
        dock.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable)
        self._root.addDockWidget(Qt.RightDockWidgetArea, dock)

    def _build_editor_dock(self):
        self.editor = QPlainTextEdit()
        font = QFont("Fira Code, Consolas, Monospace"); font.setStyleHint(QFont.Monospace)
        self.editor.setFont(font)
        self.editor.setPlaceholderText("// Open a file from the Files dock to edit.")
        dock = QDockWidget("Editor")
        dock.setWidget(self.editor)
        dock.setObjectName("EditorDock")
        dock.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable)
        self._root.addDockWidget(Qt.BottomDockWidgetArea, dock)

    def _build_files_dock(self):
        self.files_model = QFileSystemModel()
        self.files_model.setReadOnly(False)
        root_path = str(Path.cwd())
        self.files_model.setRootPath(root_path)
        self.files_tree = QTreeView()
        self.files_tree.setModel(self.files_model)
        self.files_tree.setRootIndex(self.files_model.index(root_path))
        self.files_tree.doubleClicked.connect(self._open_from_tree)

        dock = QDockWidget("Files")
        dock.setWidget(self.files_tree)
        dock.setObjectName("FilesDock")
        dock.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetClosable)
        self._root.addDockWidget(Qt.LeftDockWidgetArea, dock)

    # -------------- Connection lifecycle --------------
    def connect_to_server(self, host: str, tcp_port: int, udp_port: int, username: str, password: str, keepalive_s: int) -> str:
        """Returns server_id on success (raises on failure)."""
        self._log(f"Connecting to {host}:{tcp_port} (UDP:{udp_port}) as {username}…")

        self.network = NetworkManager(host, tcp_port, udp_port)
        self.network.connect_tcp()
        self.network.bind_udp()

        auth_message = {"username": username, "password": password, "udp_port": self.network.udp_port}
        self.network.send_tcp(auth_message)

        response = self.network.receive_tcp()
        self._log(f"TCP auth response raw: {response!r}")
        print(f"TCP auth response raw: {response!r}")
        # Try to parse single-line or first-line JSON
        try:
            server_info = json5.loads(response)
        except Exception:
            first_line = response.split("\n", 1)[0]
            server_info = json5.loads(first_line)

        server_id = server_info.get("server_id")
        if not server_id:
            raise RuntimeError(f"No server_id in response: {server_info}")

        # prepare save dir and file root
        self.server_id = server_id
        self.save_dir = Path(self._ensure_save_folder_from_server_id(server_id))
        self._set_files_root(self.save_dir)
        self.btn_upload.setEnabled(True)
        self.btn_open_save.setEnabled(True)

        # spin threads
        self.running = True
        self.keep_alive_thread = threading.Thread(target=self._send_keep_alive, args=(keepalive_s,), daemon=True)
        self.udp_thread       = threading.Thread(target=self._listen_udp, daemon=True)
        self.tcp_thread       = threading.Thread(target=self._listen_tcp, daemon=True)
        self.keep_alive_thread.start()
        self.udp_thread.start()
        self.tcp_thread.start()

        self.bus.connected.emit(server_id)
        return server_id

    def disconnect_from_server(self):
        if not self.running:
            return
        self._log("Disconnecting…")
        self.running = False
        try:
            if self.network:
                self.network.close()
        except Exception:
            pass
        for t in (self.keep_alive_thread, self.udp_thread, self.tcp_thread):
            if t:
                t.join(timeout=2)
        self.keep_alive_thread = self.udp_thread = self.tcp_thread = None
        self.bus.disconnected.emit()

    # -------------- Background loops --------------
    def _send_keep_alive(self, keep_alive_interval: int):
        while self.running:
            try:
                time.sleep(keep_alive_interval)
                if not self.running: break
                self.network.send_tcp({"type": "keep_alive"})
                self.bus.log.emit("[keep-alive] sent")
            except Exception as e:
                self.bus.log.emit(f"Keep-alive error: {e}")
                self.running = False
                break

    def _listen_udp(self):
        try:
            while self.running:
                state, _ = self.network.receive_udp()
                if isinstance(state, dict):
                    self.bus.udp_state.emit(state)
                else:
                    try:
                        import json5 as _json5
                        obj = _json5.loads(state)
                        self.bus.udp_state.emit(obj)
                    except Exception:
                        self.bus.log.emit(f"UDP non-JSON: {state!r}")
        except Exception as e:
            self.bus.log.emit(f"UDP listener error: {e}")
            self.running = False

    def _listen_tcp(self):
        buffer = ""
        while self.running:
            try:
                data = self.network.receive_tcp()
                if not data:
                    self.bus.log.emit("TCP closed by server.")
                    self.running = False
                    break
                buffer += data
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        import json5 as _json5
                        obj = _json5.loads(line)
                        self.bus.tcp_message.emit(obj)
                    except Exception:
                        self.bus.log.emit(f"TCP line (not JSON?): {line}")
            except Exception as e:
                self.bus.log.emit(f"TCP listener error: {e}")
                self.running = False
                break

    # -------------- Upload (zip chunks) --------------
    def _upload_save_folder(self):
        if not self.server_id or not self.save_dir:
            QMessageBox.information(self, "No save folder", "Connect first to get server_id and save folder.")
            return
        try:
            buffer = io.BytesIO()
            folder = self.save_dir
            with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, folder)
                        zipf.write(full_path, rel_path)
            buffer.seek(0)
            zipped_data = buffer.read()

            chunk_size = 1024
            total_chunks = (len(zipped_data) + chunk_size - 1) // chunk_size
            for i in range(total_chunks):
                if not self.running:
                    break
                chunk = zipped_data[i * chunk_size : (i + 1) * chunk_size]
                chunk_b64 = base64.b64encode(chunk).decode("utf-8")
                message = {
                    "type": "file_upload",
                    "chunk_index": i,
                    "total_chunks": total_chunks,
                    "payload_type": "zip_chunk",
                    "payload": chunk_b64
                }
                self.network.send_tcp(message)
                self._log(f"Upload chunk {i+1}/{total_chunks}")
            self._log("Upload complete.")
        except Exception as e:
            self._log(f"Upload failed: {e}\n{traceback.format_exc()}")
            QMessageBox.critical(self, "Upload failed", str(e))

    # -------------- File/editor helpers --------------
    def _set_files_root(self, path: Path):
        self.files_model.setRootPath(str(path))
        self.files_tree.setRootIndex(self.files_model.index(str(path)))

    def _editor_open(self):
        start_dir = str(self.save_dir) if self.save_dir else str(Path.cwd())
        path, _ = QFileDialog.getOpenFileName(self._root, "Open file", start_dir)
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                self.editor.setPlainText(f.read())
            self._opened_path = Path(path)
            self._log(f"Opened {path}")
        except Exception as e:
            QMessageBox.critical(self._root, "Open failed", str(e))

    def _editor_save(self):
        if not self._opened_path:
            QMessageBox.information(self._root, "No file", "Open a file first.")
            return
        try:
            with open(self._opened_path, "w", encoding="utf-8") as f:
                self.editor.setPlainText(self.editor.toPlainText())
                f.write(self.editor.toPlainText())
            self._log(f"Saved {self._opened_path}")
        except Exception as e:
            QMessageBox.critical(self._root, "Save failed", str(e))

    def _open_from_tree(self, index):
        p = self.files_model.filePath(index)
        if os.path.isdir(p):
            return
        try:
            with open(p, "r", encoding="utf-8", errors="ignore") as f:
                self.editor.setPlainText(f.read())
            self._opened_path = Path(p)
            self._log(f"Opened {p}")
        except Exception as e:
            QMessageBox.critical(self._root, "Open failed", str(e))

    def _open_save_dir(self):
        if not self.save_dir:
            QMessageBox.information(self._root, "No save folder", "Connect first to create/select a save folder.")
            return
        try:
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(self.save_dir)))
            self._log(f"Opened save folder: {self.save_dir}")
        except Exception as e:
            QMessageBox.critical(self._root, "Open folder failed", str(e))

    def _ensure_save_folder_from_server_id(self, server_id: str, template_path: str = "base_lua") -> str:
        save_path = os.path.join("saves", server_id)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            if os.path.exists(template_path):
                for item in os.listdir(template_path):
                    src = os.path.join(template_path, item)
                    dst = os.path.join(save_path, item)
                    if os.path.isfile(src):
                        shutil.copy2(src, dst)
        return save_path

    # -------------- Bus handlers / logging --------------
    def _log(self, s: str): self.bus.log.emit(s)
    def _append_log(self, s: str): self.log_view.append(s)

    def _on_connected(self, server_id: str):
        self._root.setWindowTitle(f"Game – connected to {server_id}")
        self._root.statusBar().showMessage(f"Connected to server {server_id}")

    def _on_disconnected(self):
        self._root.setWindowTitle("Game")
        self._root.statusBar().showMessage("Disconnected")
        self.btn_upload.setEnabled(False); self.btn_open_save.setEnabled(False)

    def _on_tcp_json(self, obj: dict):
        self._log(f"TCP JSON: {obj}")

    def _on_udp_state(self, state: dict):
        try:
            frame = int(state.get("frame", -1))
            if frame > self.last_frame:
                self.last_frame = frame
                # TODO: map state → canvas updates
            else:
                self._log(f"Ignored outdated frame {frame}")
        except Exception:
            self._log(f"UDP state parse issue: {state}")


# --------------------------- Root Window (stacked) ----------------------------
class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SimAntics Client")
        self.resize(1280, 820)

        self.bus = GuiBus()

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Screens
        self.menu = MainMenu()
        self.game = GameScreen(self.bus)

        self.stack.addWidget(self.menu)  # index 0
        self.stack.addWidget(self.game)  # index 1

        self.menu.join_clicked.connect(self._show_login)
        self.menu.quit_clicked.connect(self.close)

        self.setStatusBar(QStatusBar(self))

    # --- Flow ---
    def _show_login(self):
        dlg = LoginDialog(self)
        if dlg.exec() == QDialog.Accepted:
            host, tcp, udp, user, pw, ka = dlg.params()
            try:
                server_id = self.game.connect_to_server(host, tcp, udp, user, pw, ka)
                self.setWindowTitle(f"SimAntics Client – {server_id}")
                self.statusBar().showMessage(f"Connected to {host}:{tcp} (UDP:{udp}) – server {server_id}")
                self.stack.setCurrentWidget(self.game)
            except Exception as e:
                QMessageBox.critical(self, "Connect failed", f"{e}\n\n{traceback.format_exc()}")

    # Ensure disconnect on window close
    def closeEvent(self, e):
        try:
            self.game.disconnect_from_server()
        except Exception:
            pass
        finally:
            if STEAM:
                try: STEAM.unload()
                except Exception: pass
            e.accept()


# ------------------------------ main -----------------------------------------
def main():
    app = QApplication(sys.argv)
    if qdarktheme:
        try: qdarktheme.setup_theme("dark")
        except Exception: pass
    win = ClientWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

