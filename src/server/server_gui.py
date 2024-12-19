import os
import pygame
import pygame_gui
import threading
import time
from server import Server
from simulation import Simulation
from simulation_saver import SimulationSaver


class ServerGUI:
    def __init__(self):
        pygame.init()

        # Window settings
        self.window_size = (800, 600)
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("SimAntics Server")

        # Manager for GUI elements
        self.manager = pygame_gui.UIManager(self.window_size)

        self.server_running = False

        # Configuration settings
        self.simulation_config = {
            "x": 10,
            "y": 10,
            "map_update_interval": 1.0,
            "gas_update_interval": 1.0,
            "max_player_gas_count": 32,
            "save_name": "temp",
        }
        self.server_config = {
            "port": 65432,
            "udp_port": 65433,
            "inactivity_timeout": 15,
            "message_interval_rate": 5,
        }

        # Server and Simulation
        self.simulation = Simulation(
            save_name=self.simulation_config["save_name"],
            x=self.simulation_config["x"],
            y=self.simulation_config["y"],
            map_update_interval=self.simulation_config["map_update_interval"],
            gas_update_interval=self.simulation_config["gas_update_interval"],
            max_player_gas_count=self.simulation_config["max_player_gas_count"],
        )
        self.server = Server(
            simulation=self.simulation,
            host="127.0.0.1",
            port=self.server_config["port"],
            udp_port=self.server_config["udp_port"],
            inactivity_timeout=self.server_config["inactivity_timeout"],
            message_interval_rate=self.server_config["message_interval_rate"],
        )
        self.simulation.set_server(self.server)

        # Tab Container
        self.tab_container = pygame_gui.elements.UITabContainer(
            relative_rect=pygame.Rect((0, 50), (800, 550)),
            manager=self.manager,
        )
        self.config_tab_id = self.tab_container.add_tab("Config", "config_tab")
        self.run_tab_id = self.tab_container.add_tab("Run", "run_tab")

        # Create tabs
        self.create_config_tab()
        self.create_run_tab()

        # Control flags
        self.popup_window = None
        self.running = True

    def create_config_tab(self):
        """Create the configuration tab with load/save functionality."""
        config_tab_panel = self.tab_container.get_tab_container(self.config_tab_id)

        # Simulation Config Fields
        self.simulation_fields = self.create_config_fields(
            self.simulation_config, config_tab_panel, y_offset=10
        )

        # Server Config Fields
        self.server_fields = self.create_config_fields(
            self.server_config, config_tab_panel, y_offset=250
        )

        # Load Save Button
        self.load_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((250, 450), (150, 50)),
            text="Load Save",
            manager=self.manager,
            container=config_tab_panel,
        )

    def create_run_tab(self):
        """Create the run tab with server controls."""
        run_tab_panel = self.tab_container.get_tab_container(self.run_tab_id)

        # Start/Stop Server Button
        self.start_stop_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 400), (150, 50)),
            text="Run Server",
            manager=self.manager,
            container=run_tab_panel,
        )

        # Save Simulation Button
        self.save_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((250, 400), (150, 50)),
            text="Save Simulation",
            manager=self.manager,
            container=run_tab_panel,
        )

        # Logs Panel
        self.logs_panel = pygame_gui.elements.ui_text_box.UITextBox(
            relative_rect=pygame.Rect((50, 10), (700, 300)),
            html_text="Logs will appear here...",
            manager=self.manager,
            container=run_tab_panel,
        )

    def create_config_fields(self, config, container, y_offset):
        """Create text input fields for configuration settings."""
        fields = {}
        for index, (key, value) in enumerate(config.items()):
            label = pygame_gui.elements.UILabel(
                relative_rect=pygame.Rect((50, y_offset + index * 40), (200, 30)),
                text=f"{key}:",
                manager=self.manager,
                container=container,
            )
            input_field = pygame_gui.elements.UITextEntryLine(
                relative_rect=pygame.Rect((250, y_offset + index * 40), (200, 30)),
                manager=self.manager,
                container=container,
            )
            input_field.set_text(str(value))

            if self.server_running:
                input_field.disable()
            else:
                input_field.enable()
            fields[key] = input_field
        return fields

    def populate_fields(self, fields, config):
        """Update GUI fields with values from the config."""
        for key, field in fields.items():
            field.set_text(str(config[key]))

    def toggle_config_fields(self, enable):
        """
        Enable or disable all configuration fields.

        Args:
            enable (bool): If True, enable the fields; if False, disable them.
        """
        for field in self.simulation_fields.values():
            if enable:
                field.enable()
            else:
                field.disable()

        for field in self.server_fields.values():
            if enable:
                field.enable()
            else:
                field.disable()

    def start_stop_server(self):
        if not self.server_running:
            """Initialize and start the server."""
            self.start_stop_button.set_text("...")

            # Disable configuration fields
            self.toggle_config_fields(False)

            # Read updated configuration
            self.read_config_fields(self.simulation_fields, self.simulation_config)
            self.read_config_fields(self.server_fields, self.server_config)

            # Update simulation and server based on the configuration
            self.simulation = Simulation(
                save_name=self.simulation_config["save_name"],
                x=self.simulation_config["x"],
                y=self.simulation_config["y"],
                map_update_interval=self.simulation_config["map_update_interval"],
                gas_update_interval=self.simulation_config["gas_update_interval"],
                max_player_gas_count=self.simulation_config["max_player_gas_count"],
            )
            self.server = Server(
                simulation=self.simulation,
                host="127.0.0.1",
                port=self.server_config["port"],
                udp_port=self.server_config["udp_port"],
                inactivity_timeout=self.server_config["inactivity_timeout"],
                message_interval_rate=self.server_config["message_interval_rate"],
            )
            self.simulation.set_server(self.server)

            # Start server and simulation
            self.simulation_thread = threading.Thread(target=self.simulation.start, args=[self.server.outbound_queue], daemon=True)
            self.simulation_thread.start()

            self.server_thread = threading.Thread(target=self.server.run, daemon=True)
            self.server_thread.start()

            self.server_running = True
            self.update_logs("Server started.")

            self.start_stop_button.set_text("Stop Server")

        else:
            """Stop both server and simulation."""
            self.start_stop_button.set_text("...")

            self.simulation.stop()
            self.server.stop()
            self.server_running = False

            # Enable configuration fields
            self.toggle_config_fields(True)

            self.update_logs("Server stopped.")
            self.start_stop_button.set_text("Start Server")

    def read_config_fields(self, fields, config):
        """Update config dictionary with values from GUI input fields."""
        for key, field in fields.items():
            try:
                config[key] = type(config[key])(field.get_text())
            except ValueError:
                self.update_logs(f"[Error] Invalid value for {key}. Using default: {config[key]}")

    def load_save(self):
        """Create a popup for selecting a save folder."""
        if self.popup_window:
            return  # Prevent multiple popups

        saves_dir = "saves"
        if not os.path.exists(saves_dir):
            os.makedirs(saves_dir)

        save_folders = [
            folder for folder in os.listdir(saves_dir) if os.path.isdir(os.path.join(saves_dir, folder))
        ]

        # Popup window
        popup_rect = pygame.Rect((200, 150), (400, 300))
        self.popup_window = pygame_gui.elements.UIWindow(
            rect=popup_rect,
            manager=self.manager,
            window_display_title="Load Save",
        )

        save_list = pygame_gui.elements.UISelectionList(
            relative_rect=pygame.Rect((20, 20), (360, 200)),
            item_list=save_folders,
            manager=self.manager,
            container=self.popup_window,
        )

        ok_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, 240), (100, 40)),
            text="OK",
            manager=self.manager,
            container=self.popup_window,
        )

        cancel_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((140, 240), (100, 40)),
            text="Cancel",
            manager=self.manager,
            container=self.popup_window,
        )

        def handle_load_save(event):
            nonlocal save_list
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == ok_button:
                    selected = save_list.get_single_selection()
                    if selected:
                        self.popup_window.kill()
                        self.popup_window = None
                        self.simulation_config["save_name"] = selected

                        self.server = SimulationSaver.load_simulation(self.simulation, selected)
                        self.populate_fields(self.simulation_fields, self.simulation_config)
                        self.populate_fields(self.server_fields, self.server_config)
                        self.update_logs(f"Selected save: {selected}")

                elif event.ui_element == cancel_button:
                    self.popup_window.kill()
                    self.popup_window = None

        self.popup_window_process_event = handle_load_save

    def save_simulation(self):
        """Save the current simulation and server state."""
        # Read the save_name field from the GUI input
        self.read_config_fields(self.simulation_fields, self.simulation_config)
        
        save_name = self.simulation_config["save_name"]
        SimulationSaver.save_simulation(self.simulation, save_name)
        self.update_logs(f"Simulation saved to: {save_name}")

    def update_logs(self, message):
        """Update the logs panel."""
        current_text = self.logs_panel.html_text
        updated_text = current_text + f"<br>{message}"
        self.logs_panel.kill()  # Remove the old text box
        self.logs_panel = pygame_gui.elements.ui_text_box.UITextBox(
            relative_rect=pygame.Rect((50, 10), (700, 300)),
            html_text=updated_text,
            manager=self.manager,
            container=self.tab_container.get_tab_container(self.run_tab_id),
        )

    def run(self):
        """Main loop."""
        clock = pygame.time.Clock()

        while self.running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.start_stop_button:
                        self.start_stop_server()
                    elif event.ui_element == self.load_button:
                        self.load_save()
                    elif event.ui_element == self.save_button:
                        self.save_simulation()

                if self.popup_window and hasattr(self, "popup_window_process_event"):
                    self.popup_window_process_event(event)

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.window.fill((0, 0, 0))  # Clear the screen with black
            self.manager.draw_ui(self.window)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    gui = ServerGUI()
    gui.run()
