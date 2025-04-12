import pygame
import pygame_gui

from escapable_popup import EscapablePopup

class LoginPopup(EscapablePopup):
    def setup_ui(self):
        self.size = (350, 300)
        self.make_popup_window()
        
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
        self.connect_tcp_port_input.set_text("65432")

        self.connect_udp_port_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((75, 120), (200, 30)),
            manager=self.gui.gui_manager,
            container=self.window
        )
        self.connect_udp_port_input.set_text("65433")

        self.connect_password_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((75, 160), (200, 30)),
            manager=self.gui.gui_manager,
            container=self.window
        )
        self.connect_password_input.set_text_hidden(True)

        self.connect_submit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((125, self.size[1] - 110), (100, 40)),
            text="Connect",
            manager=self.gui.gui_manager,
            container=self.window
        )


        self.gui.ui_element_actions[self.connect_submit_button] = self.on_connect_submit
        
        self.focus_order = [self.connect_ip_input, self.connect_tcp_port_input, self.connect_udp_port_input, self.connect_password_input, self.connect_submit_button, self.default_button]
        self.default_focus_index = 3
        self.focus_default_element()

    def on_return_default(self):
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
            self.cancel()
            self.gui.init_workspace()
        except Exception as e:
            print(f"Failed to connect: {e}")
            if hasattr(self, 'client') and self.client:
                self.client.shutdown()
            self.client = None
        finally:
            self.connect_submit_button.enable()