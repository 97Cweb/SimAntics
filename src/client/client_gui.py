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

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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
            self.handle_events()
            self.gui_manager.update(time_delta)
            self.draw()
            
        pygame.quit()
        self.steamworks.unload()
        del self.steamworks
        sys.exit()

    # Button Actions
    def on_save_clicked(self):
        print("Save clicked")

    def on_return_clicked(self):
        views.create_game_ui(self)

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
        except Exception as e:
            print(f"Failed to connect: {e}")
            self.status_label.set_text("Connection failed")
        finally:
            self.connect_submit_button.enable()





if __name__ == "__main__":
    gui = ClientGUI()
    gui.run()
