import pygame
import pygame_gui
import sys

from client import Client
import client_ui_views as views


from steamworks import STEAMWORKS

class ClientGUI:
    def __init__(self):
        self.init_steam()
        pygame.init()

        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags=pygame.SCALED)
        pygame.display.set_caption("Simantics Client")

        self.gui_manager = pygame_gui.UIManager((self.screen_width, self.screen_height))

        self.client = None

        self.ui_elements = []
        self.ui_element_actions = {}

        views.create_main_menu_ui(self)

        self.running = True
        self.quit_window = None
        self.connect_window = None
        

    def init_steam(self):
        #setup steamworks
        self.steamworks = STEAMWORKS()
        self.steamworks.initialize()
        if (self.steamworks.UserStats.RequestCurrentStats() == True):
            print('Stats successfully retrieved!')
        

    def clear_ui(self):
        for element in self.ui_elements:
            element.kill()
        self.ui_elements = []
        self.ui_element_actions = {}

    def show_quit_dialog(self):
        views.create_quit_dialog(self)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.client: 
                    self.client.shutdown()
                self.running = False


            # Let file bar handle any events it owns (rename popup, etc.)
            if hasattr(self, 'file_bar_view'):
                self.file_bar_view.handle_event(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.connect_window and self.connect_window.alive():
                    self.connect_window.kill()
                    self.connect_window = None
                elif self.quit_window and self.quit_window.alive():
                    views.close_quit_popup(self)
                else:
                    self.show_quit_dialog()

            elif event.type == pygame_gui.UI_WINDOW_CLOSE:
                if event.ui_element == self.connect_window:
                    self.connect_window.kill()
                    self.connect_window = None
                elif event.ui_element == self.quit_window:
                    views.close_quit_popup(self)
                    
            elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element in [self.connect_password_input, self.connect_tcp_port_input, self.connect_udp_port_input]:
                    self.on_connect_submit()

            

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                action = self.ui_element_actions.get(event.ui_element)
                if action:
                    action()


            
            self.gui_manager.process_events(event)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.gui_manager.draw_ui(self.screen)
        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            time_delta = clock.tick(60) / 1000.0
            
            if self.client and not self.client.running and self.state == "game":
                views.create_main_menu_ui(self)
            self.handle_events()
            self.gui_manager.update(time_delta)
            self.draw()
            
        pygame.quit()
        self.steamworks.unload()
        del self.steamworks
        sys.exit()

    # Button Actions
    def on_save_clicked(self):
        if hasattr(self, "open_file_path"):
            try:
                html_text = self.editor_box.html_text
                # Remove HTML tags if needed or store as-is
                with open(self.open_file_path, "w", encoding="utf-8") as f:
                    f.write(html_text)
                print(f"Saved: {self.open_file_path}")
            except Exception as e:
                print(f"Failed to save: {e}")


    def on_return_clicked(self):
        current_text = self.editor_box.html_text
        if hasattr(self, "original_text") and current_text != self.original_text:
            self.show_save_reminder_popup()
        else:
            from client_ui_views import create_game_ui
            create_game_ui(self)
            self.file_bar_view.upload_callback = self.client.upload_save_folder



    def on_quit_os_clicked(self):
        self.client.shutdown()
        self.running = False

    def on_quit_main_menu_clicked(self):
        self.client.shutdown()
        views.close_quit_popup(self)
        views.create_main_menu_ui(self)

    def on_quit_cancel_clicked(self):
        views.close_quit_popup(self)
        
    def on_connect_clicked(self):
        views.create_connect_dialog(self)
        
    def on_connect_submit(self):
        password = self.connect_password_input.get_text()
        ip = self.connect_ip_input.get_text()
        tcp_port = int(self.connect_tcp_port_input.get_text())
        udp_port = int(self.connect_udp_port_input.get_text())
        self.connect_submit_button.disable()
        try:
            self.client = Client(self.steamworks, password=password, host=ip, tcp_port=tcp_port, udp_port=udp_port)
            self.status_label.set_text("Status: Connected")
            self.connect_window.kill()
            self.connect_window = None
            views.create_game_ui(self)
            self.file_bar_view.upload_callback = self.client.upload_save_folder

        except Exception as e:
            print(f"Failed to connect: {e}")
            self.status_label.set_text("Connection failed")
        finally:
            self.connect_submit_button.enable()



    def on_file_clicked(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            from client_ui_views import create_editor_ui
            create_editor_ui(self)
            self.editor_box.set_text(content)
            self.open_file_path = file_path  # Store to use on save
            self.original_text = content  
        except Exception as e:
            print(f"Failed to open file {file_path}: {e}")

    def show_save_reminder_popup(self):
        if hasattr(self, "save_reminder_window"):
            return
    
        self.save_reminder_window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect((250, 200), (300, 150)),
            manager=self.gui_manager,
            window_display_title="Unsaved Changes"
        )
    
        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((20, 20), (260, 30)),
            text="Save changes before returning?",
            manager=self.gui_manager,
            container=self.save_reminder_window
        )
    
        save_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, 70), (80, 30)),
            text="Save",
            manager=self.gui_manager,
            container=self.save_reminder_window
        )
    
        discard_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((110, 70), (80, 30)),
            text="Discard",
            manager=self.gui_manager,
            container=self.save_reminder_window
        )
    
        cancel_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((200, 70), (80, 30)),
            text="Cancel",
            manager=self.gui_manager,
            container=self.save_reminder_window
        )
    
        self.ui_element_actions[save_btn] = self._on_save_reminder_save
        self.ui_element_actions[discard_btn] = self._on_save_reminder_discard
        self.ui_element_actions[cancel_btn] = self._on_save_reminder_cancel


    def _on_save_reminder_save(self):
        self.on_save_clicked()
        self.original_text = self.editor_box.get_text()  # Update after saving
        self._close_save_reminder()
        self.on_return_clicked()
    
    def _on_save_reminder_discard(self):
        self.original_text = self.editor_box.get_text()  # Accept current state as baseline
        self._close_save_reminder()
        from client_ui_views import create_game_ui
        create_game_ui(self)
        self.file_bar_view.upload_callback = self.client.upload_save_folder

    
    def _on_save_reminder_cancel(self):
        self._close_save_reminder()
    
    def _close_save_reminder(self):
        if hasattr(self, "save_reminder_window") and self.save_reminder_window.alive():
            self.save_reminder_window.kill()
        self.save_reminder_window = None


if __name__ == "__main__":
    gui = ClientGUI()
    gui.run()
