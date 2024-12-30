import os
import pygame
import pygame_gui
import threading
import logging

from simantics_common.mod_manager import ModManager

from server import Server
from simulation import Simulation
from simulation_saver import SimulationSaver
from server_gui_log_handler import ServerGUILogHandler




# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Default log level
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)  # Use the module's name for the logger
class ServerGUI:
    def __init__(self):
        pygame.quit()
        pygame.init()
        pygame.font.quit()
        pygame.font.init()
        

        # Window settings
        self.window_size = (800, 600)
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("SimAntics Server")

        # Manager for GUI elements
        self.manager = pygame_gui.UIManager(self.window_size)

        self.server_running = False

        # Configuration settings
        self.simulation_config = {
            "save_name": "",
            "x": "",
            "y": "",
            "map_update_interval": "",
            "gas_update_interval": "",
            "max_player_gas_count": "",
            
        }
        self.server_config = {
            "port": "",
            "udp_port": "",
            "inactivity_timeout": "",
            "message_interval_rate": "",
        }
        
        
        
        if any(isinstance(h, ServerGUILogHandler) for h in logger.handlers):
            # Remove the old handler
            for h in logger.handlers:
                if isinstance(h, ServerGUILogHandler):
                    logger.removeHandler(h)
                    h.close()  # Close the old handler properly
        
        # Add a new handler
       # GUI Log Handler
        self.temp_log_buffer = []  # Temporary buffer for logs
        gui_handler = ServerGUILogHandler(self)
        gui_handler.setLevel(logging.INFO)
        logger.addHandler(gui_handler)
        self.gui_handler = gui_handler
        
        
        self.inactive_mod_list_gui = None
        self.active_mod_list_gui = None   
        
        self.inactive_mods = []  # Initialize as empty list
        self.active_mods = []    # Initialize as empty list
        
        
        # Server and Simulation
        self.simulation = None
        self.server = None
        
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

        self.load_mods()

        # Control flags
        self.popup_window = None
        self.running = True
        
        
        
    
    def load_mods(self):
        """
        Load mods using ModManager and update GUI lists.
        """

        save_name = self.simulation_config["save_name"]
        mods_config = ModManager.load_mod_config(save_name)
        available_mods = ModManager.scan_mods_folder()

        self.active_mods, self.inactive_mods = ModManager.get_mod_status(mods_config, available_mods)
        


        self.update_mod_ui()

    
         
    def update_mod_ui(self):
        # Update GUI lists
        if self.inactive_mod_list_gui and self.active_mod_list_gui:
            self.inactive_mod_list_gui.set_item_list(self.inactive_mods)
            self.active_mod_list_gui.set_item_list(self.active_mods)
        

        


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
        
        # Mods Panel
        mods_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((500, 10), (280, 400)),
            manager=self.manager,
            container=config_tab_panel,
        )
        
        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((10, 10), (260, 30)),
            text="Mods Configuration:",
            manager=self.manager,
            container=mods_panel,
        )

        self.inactive_mod_list_gui = pygame_gui.elements.UISelectionList(
            relative_rect=pygame.Rect((10, 50), (120, 300)),
            item_list=self.inactive_mods,
            manager=self.manager,
            container=mods_panel,
        )

        self.active_mod_list_gui = pygame_gui.elements.UISelectionList(
            relative_rect=pygame.Rect((150, 50), (120, 300)),
            item_list=[mod["name"] for mod in self.active_mods],
            manager=self.manager,
            container=mods_panel,
        )

        # Load Save Button
        self.load_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((250, 450), (150, 50)),
            text="Load Save",
            manager=self.manager,
            container=config_tab_panel,
        )
        
        # New Game Button
        self.new_game_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 450), (150, 50)),
            text="New Game",
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
        
        self.save_button.disable()  # Initially disable the save button
        
        self.log_level_dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list=["DEBUG", "INFO", "WARNING", "ERROR"],
            starting_option="INFO",
            relative_rect=pygame.Rect((450, 400), (200, 30)),
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
    
    def handle_mod_transfer(self, event):
        """Handle moving mods between active and inactive lists."""
        if event.type == pygame_gui.UI_SELECTION_LIST_DOUBLE_CLICKED_SELECTION:
            
            if event.ui_element == self.inactive_mod_list_gui:
                mod_name = self.inactive_mod_list_gui.get_single_selection()
                if mod_name:
                    self.active_mods.append(mod_name)
                    self.inactive_mods.remove(mod_name)
                    self.update_mod_ui()
            elif event.ui_element == self.active_mod_list_gui:
                mod_name = self.active_mod_list_gui.get_single_selection()
                if mod_name:
                    self.inactive_mods.append(mod_name)
                    self.inactive_mods.sort()
                    self.active_mods.remove(mod_name)
                    self.update_mod_ui()
            
                    

    def create_config_fields(self, config, container, y_offset):
        """Create text input fields for configuration settings."""
        fields = {}
        for index, (key, value) in enumerate(config.items()):
            pygame_gui.elements.UILabel(
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
                
    def create_new_game(self):
        """Prompt for a new game save name and reset configuration."""
        if self.popup_window:
            return  # Prevent multiple popups

        popup_rect = pygame.Rect((200, 150), (400, 200))
        self.popup_window = pygame_gui.elements.UIWindow(
            rect=popup_rect,
            manager=self.manager,
            window_display_title="New Game",
        )

        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, 20), (360, 30)),
            text="Enter Save Name:",
            manager=self.manager,
            container=self.popup_window,
        )

        save_name_entry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((20, 60), (360, 30)),
            manager=self.manager,
            container=self.popup_window,
        )

        ok_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, 120), (100, 40)),
            text="OK",
            manager=self.manager,
            container=self.popup_window,
        )

        cancel_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((140, 120), (100, 40)),
            text="Cancel",
            manager=self.manager,
            container=self.popup_window,
        )

        def handle_new_game(event):
            nonlocal save_name_entry
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == ok_button:
                    save_name = save_name_entry.get_text()
                    if save_name:
                        self.simulation_config = {
                            "save_name": save_name,
                            "x": 10,
                            "y": 10,
                            "map_update_interval": 1.0,
                            "gas_update_interval": 1.0,
                            "max_player_gas_count": 32,
                            
                        }
                        self.server_config = {
                            "port": 65432,
                            "udp_port": 65433,
                            "inactivity_timeout": 15,
                            "message_interval_rate": 5,
                        }

                        self.populate_fields(self.simulation_fields, self.simulation_config)
                        self.populate_fields(self.server_fields, self.server_config)
                        self.load_mods()
                        self.update_logs(f"New game created with save name: {save_name}")
                        self.load_from_save = False


                    self.popup_window.kill()
                    self.popup_window = None

                elif event.ui_element == cancel_button:
                    self.popup_window.kill()
                    self.popup_window = None

        self.popup_window_process_event = handle_new_game

    def start_stop_server(self):
        if not self.server_running:
            """Initialize and start the server."""
            
            # Validate mods
            available_mods = ModManager.scan_mods_folder()
            missing_mods = [mod for mod in self.active_mods if  mod not in [item for item in available_mods]]
            if missing_mods:
                proceed_anyway = self.show_missing_mods_popup(missing_mods)
                if not proceed_anyway:
                    return
           
            self.start_stop_button.set_text("...")

            # Disable configuration fields
            self.toggle_config_fields(False)

            # Read updated configuration
            self.read_config_fields(self.simulation_fields, self.simulation_config)
            self.read_config_fields(self.server_fields, self.server_config)

            # Update simulation and server based on the configuration
            

            self.simulation = Simulation(
                simulation_config=self.simulation_config,
                mods = self.active_mods,
                load_from_save=self.load_from_save
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
            self.simulation.add_log_handler(self.gui_handler)
            

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
            
    def show_missing_mods_popup(self, missing_mods):
        """Show a popup with missing mods."""
        if self.popup_window:
            return  # Prevent multiple popups

        popup_rect = pygame.Rect((200, 150), (400, 300))
        self.popup_window = pygame_gui.elements.UIWindow(
            rect=popup_rect,
            manager=self.manager,
            window_display_title="Missing Mods",
        )

        mod_list = "<br>".join(missing_mods)
        message = f"The following mods are missing:<br>{mod_list}"

        pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((20, 20), (360, 200)),
            html_text=message,
            manager=self.manager,
            container=self.popup_window,
        )

        continue_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, 240), (100, 40)),
            text="Continue",
            manager=self.manager,
            container=self.popup_window,
        )

        cancel_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((140, 240), (100, 40)),
            text="Cancel",
            manager=self.manager,
            container=self.popup_window,
        )

        def handle_missing_mods(event):
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == continue_button:
                    self.popup_window.kill()
                    self.popup_window = None
                    return True
                elif event.ui_element == cancel_button:
                    self.popup_window.kill()
                    self.popup_window = None
                    return False

        self.popup_window_process_event = handle_missing_mods


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

                        # Use SimulationSaver to fetch configs
                        simulation_config, server_config = SimulationSaver.get_simulation_config(selected)
                        self.simulation_config.update(simulation_config)
                        self.server_config.update(server_config)
                        self.populate_fields(self.simulation_fields, self.simulation_config)
                        self.populate_fields(self.server_fields, self.server_config)
                        self.load_mods()
                        self.update_logs(f"Selected save: {selected}")
                        self.load_from_save = True

                elif event.ui_element == cancel_button:
                    self.popup_window.kill()
                    self.popup_window = None

        self.popup_window_process_event = handle_load_save

    def save_simulation(self):
        """Save the current simulation and server state."""
        # Read the save_name field from the GUI input
        self.read_config_fields(self.simulation_fields, self.simulation_config)
        
        save_name = self.simulation_config["save_name"]
        SimulationSaver.save_simulation(self.simulation)
        self.update_logs(f"Simulation saved to: {save_name}")

    def update_logs(self, message):
        """Update the logs panel."""
        current_text = self.logs_panel.html_text
        updated_text = f"{current_text}<br>{message}"
        self.logs_panel.set_text(updated_text)

    def validate_config(self):
        """Validate if all required configuration fields are filled."""
        try:
            for key, field in self.simulation_fields.items():
                if key in ["x", "y"] and self.load_from_save:
                    # Grey out the x and y fields if loading from a file
                    field.disable()
                else:
                    field.enable()
    
                # Skip validation for x and y if loading from save
                if not (key in ["x", "y"] and self.load_from_save) and field.get_text() == "":
                    return False
    
            for key, field in self.server_fields.items():
                if field.get_text() == "":
                    return False
    
            return True
        except Exception as e:
            self.update_logs(f"[Error] Validation failed: {e}")
            return False


        
    def shutdown(self):
        """
        Clean up resources and detach the log handler.
        """
        if hasattr(self, "gui_handler") and self.gui_handler in logger.handlers:
            logger.removeHandler(self.gui_handler)
            self.gui_handler.close()
    
        # Clean up pygame resources
        pygame.display.quit()
        pygame.font.quit()
        pygame.quit()



    def run(self):
        """Main loop."""
        clock = pygame.time.Clock()
        self.start_stop_button.disable()  # Initially disable the button
        
        
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
                    elif event.ui_element == self.new_game_button:
                        self.create_new_game()
                elif event.type == pygame_gui.UI_SELECTION_LIST_DOUBLE_CLICKED_SELECTION:
                    self.handle_mod_transfer(event)

                if self.popup_window and hasattr(self, "popup_window_process_event"):
                    self.popup_window_process_event(event)
                    
                if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED and event.ui_element == self.log_level_dropdown:
                    selected_level = self.log_level_dropdown.selected_option[0]  # Ensure selected_level is a string
                    if hasattr(logging, selected_level):  # Check if the selected level is valid
                        self.gui_handler.setLevel(getattr(logging, selected_level))
                        logger.info(f"Log level changed to {selected_level}")
                    else:
                        logger.warning(f"Invalid log level selected: {selected_level}")

            
                if self.validate_config():
                    self.start_stop_button.enable()
                else:
                    self.start_stop_button.disable()
                    
                if self.simulation:
                    self.save_button.enable()
                else:
                    self.save_button.disable()
                        
                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.window.fill((0, 0, 0))  # Clear the screen with black
            self.manager.draw_ui(self.window)
            pygame.display.update()
            
            


        self.shutdown()


if __name__ == "__main__":
    gui = ServerGUI()
    gui.run()
