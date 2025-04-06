import pygame
import pygame_gui
import threading
from client import Client

from simantics_SteamworksWrapper.steamworks_bindings import steam_lib 

class ClientGUI:
    def __init__(self):
        pygame.init()

        # Screen setup
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), flags = pygame.SCALED)
        pygame.display.set_caption("Client GUI")

        # Pygame GUI Manager
        self.gui_manager = pygame_gui.UIManager((self.screen_width, self.screen_height))

        # UI Components
        self.status_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((10, 10), (200, 30)),
            text="Status: Disconnected",
            manager=self.gui_manager,
        )
        self.connect_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((10, 50), (150, 30)),
            text="Connect",
            manager=self.gui_manager,
        )
        self.chat_box = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((10, 100), (780, 400)),
            html_text="",
            manager=self.gui_manager,
        )
        self.message_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((10, 520), (600, 30)),
            manager=self.gui_manager,
        )
        self.send_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((620, 520), (150, 30)),
            text="Send",
            manager=self.gui_manager,
        )
        
        # Steamworks setup
        self.steam_initialized = False
        self.init_steam()

        # Client setup
        self.client = Client()
        self.running = True

        # Thread for network communication
        self.network_thread = threading.Thread(target=self.run_client, daemon=True)
        



    def run_client(self):
        """Start the client connection and listen for updates."""
        try:
            self.client.connect(username="cb", password="pw")
        except Exception as e:
            print(f"Client error: {e}")

    def handle_events(self):
        """Handle Pygame and GUI events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.client.shutdown()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.connect_button:
                    self.status_label.set_text("Status: Connected")
                    if not self.network_thread.is_alive():
                        self.network_thread.start()
                elif event.ui_element == self.send_button:
                    message = self.message_input.get_text()
                    self.client.network.send_tcp({"type": "message", "content": message})
                    self.chat_box.append_html_text(f"<b>You:</b> {message}<br>")
                    self.message_input.set_text("")
            self.gui_manager.process_events(event)
            
    def update(self, time_delta):
        self.gui_manager.update(time_delta)
        if self.steam_initialized:
            steam_lib.run_callbacks()  # Ensure Steamworks callbacks are processed
        
    def draw(self, surface):
        surface.fill((0, 0, 0))  # Black background
        self.gui_manager.draw_ui(surface)
        pygame.display.flip()
        
    def run(self):
        """Main loop for the GUI."""
        clock = pygame.time.Clock()

        while self.running:
            time_delta = clock.tick(60) / 1000.0
            self.handle_events()
            
            self.update(time_delta)
            self.draw(self.screen)
            

        pygame.quit()

if __name__ == "__main__":
    gui = ClientGUI()
    gui.run()
