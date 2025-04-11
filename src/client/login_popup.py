import pygame
import pygame_gui

from escapable_popup import EscapablePopup

class LoginPopup(EscapablePopup):
    def setup_ui(self):
        self.size = (350, 300)
        super().setup_ui()
        width, height = self.size

        self.connect_ip_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((75, 40), (200, 30)),
            manager=self.gui.gui_manager,
            container=self.window
        )
        self.connect_ip_input.set_text("127.0.0.1")

        self.connect_tcp_port_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((75, 80), (200, 30)),
            manager=self.gui.gui_manager,
            container=self.window
        )
        self.connect_tcp_port_input.set_text("8765")

        self.connect_udp_port_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((75, 120), (200, 30)),
            manager=self.gui.gui_manager,
            container=self.window
        )
        self.connect_udp_port_input.set_text("5678")

        self.connect_password_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((75, 160), (200, 30)),
            manager=self.gui.gui_manager,
            container=self.window
        )
        self.connect_password_input.set_text_hidden(True)
        self.connect_password_input.focus()

        self.connect_submit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((125, height - 110), (100, 40)),
            text="Connect",
            manager=self.gui.gui_manager,
            container=self.window
        )

        self.gui.ui_element_actions[self.connect_submit_button] = self.on_connect_submit

    def on_return(self):
        self.on_connect_submit()


    def on_connect_submit(self):
        password = self.connect_password_input.get_text()
        ip = self.connect_ip_input.get_text()
        tcp_port = int(self.connect_tcp_port_input.get_text())
        udp_port = int(self.connect_udp_port_input.get_text())
        self.connect_submit_button.disable()
        try:
            from client import Client
            self.client = Client(self.gui.steamworks, password=password, host=ip, tcp_port=tcp_port, udp_port=udp_port)
            self.gui.status_label.set_text("Status: Connected")
            self.cancel()
            from views import create_game_ui
            create_game_ui(self.gui)
            self.gui.file_bar_view.upload_callback = self.client.upload_save_folder
        except Exception as e:
            print(f"Failed to connect: {e}")
        finally:
            self.connect_submit_button.enable()