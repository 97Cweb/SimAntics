import sys
import pygame
import pygame_gui

from steamworks import STEAMWORKS
from layout_manager import LayoutManager
from quit_from_menu_popup import QuitFromMenuPopup
from login_popup import LoginPopup

class ClientGUI:
    def __init__(self):
        self.init_steam()
    
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("Simantics Client")

        self.gui_manager = pygame_gui.UIManager((self.screen_width, self.screen_height))

        self.clock = pygame.time.Clock()
        self.running = True

        self.state = "main_menu"  # Options: main_menu, workspace

        self.ui_elements = []
        self.layout = None
        
        self.active_popup = None

        self.init_main_menu()   
        
    def init_steam(self):
        #setup steamworks
        self.steamworks = STEAMWORKS()
        self.steamworks.initialize()

    # -------------------- State Setup --------------------

    def init_main_menu(self):
        self.clear_ui()
        self.state = "main_menu"

        title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((300, 150), (200, 50)),
            text="Main Menu",
            manager=self.gui_manager,
        )

        start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((325, 250), (150, 50)),
            text="Join Game",
            manager=self.gui_manager,
        )

        quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((325, 320), (150, 50)),
            text="Quit",
            manager=self.gui_manager,
        )

        self.ui_elements.extend([title, start_button, quit_button])
        self.ui_element_actions = {
            start_button: lambda: LoginPopup(self),
            quit_button: self.quit,
        }

    def init_workspace(self):
        self.clear_ui()
        self.state = "workspace"
        self.layout = LayoutManager(self)

    def quit(self):
        self.running = False

    def clear_ui(self):
        for el in self.ui_elements:
            el.kill()
        self.ui_elements = []
        self.ui_element_actions = {}
        if self.layout:
            self.layout.destroy_all()
            self.layout = None

    # -------------------- Main Loop --------------------

    def handle_events(self):
        for event in pygame.event.get():
            
            


            if event.type == pygame.QUIT:
                self.quit()
                
            if self.layout and event.type == pygame.MOUSEMOTION:
                self.layout.views["game"].update_cursor(event.pos)

                
            elif event.type == pygame.VIDEORESIZE:
                self.screen_width, self.screen_height = event.w, event.h
                self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
                self.gui_manager.set_window_resolution((self.screen_width, self.screen_height))
                if self.layout:
                    self.layout.on_resize()

            elif event.type == pygame.KEYDOWN:
                if self.state == "workspace":
                    if event.key == pygame.K_TAB and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.layout.focus_next_view()
                    # Add Tab-inside-panel support here if needed
                    
                elif self.state == "main_menu":
                    if event.key == pygame.K_ESCAPE:
                        if self.active_popup is None:
                            QuitFromMenuPopup(self)
                        else:
                            self.active_popup.escape()

    
            elif event.type == pygame_gui.UI_WINDOW_CLOSE: 
                if self.active_popup:
                    if event.ui_element == self.active_popup.window:
                        self.active_popup.cancel()

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element in self.ui_element_actions:
                    self.ui_element_actions[event.ui_element]()
                    
            elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if self.active_popup and hasattr(self.active_popup, 'on_return'):
                    self.active_popup.on_return()


            
            self.gui_manager.process_events(event)
            
            if self.layout:
                self.layout.handle_event(event)
               
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.gui_manager.draw_ui(self.screen)
        pygame.display.update()

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.gui_manager.update(time_delta)

            # Optionally update views
            if self.layout:
                for view in self.layout.views.values():
                    view.update(time_delta)
            
            self.draw()
            

        pygame.quit()
        self.steamworks.unload()
        sys.exit()


if __name__ == "__main__":
    gui = ClientGUI()
    gui.run()