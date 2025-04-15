import sys
import pygame
import pygame_gui

from steamworks import STEAMWORKS

from focusable_group import FocusableGroup
from layout_manager import LayoutManager
from login_popup import LoginPopup
from quit_from_game_popup import QuitFromGamePopup
from quit_from_menu_popup import QuitFromMenuPopup


class ClientGUI(FocusableGroup):
    def __init__(self):
        self.init_steam()
        
        super().__init__()
    
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("Simantics Client")

        self.gui_manager = pygame_gui.UIManager((self.screen_width, self.screen_height), theme_path="theme.json")

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
        pygame.event.clear()
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
        self.ui_element_actions[start_button] = self._open_login_popup
        self.ui_element_actions[quit_button] = self.quit
        
        self.focus_order = [start_button, quit_button]
        self.default_focus_index = 0
        self.focus_default_element()


        
    def _open_login_popup(self):
        
        if self.active_popup is None:
            print("opening")
            LoginPopup(self)
            
    def focus_next_element(self, reverse=False):
        if self.active_popup:
            self.active_popup.focus_next(reverse)
        elif self.state == "main_menu":
            self.focus_next(reverse)
        elif self.state == "workspace" and self.layout:
            self.layout.focus_next(reverse)

    def is_text_input_active(self):
        if self.layout and self.layout.current_selected:
            el = self.layout.current_selected.current_selected
            return isinstance(el, pygame_gui.elements.UITextEntryBox) and el.is_focused
        return False


    def init_workspace(self):
        self.clear_ui()
        self.state = "workspace"
        self.layout = LayoutManager(self)

    def quit(self):
        self.running = False

    def clear_ui(self):
        
        if self.active_popup:
            self.active_popup.cancel()  # 🔧 Make sure this is here
        
        for el in self.ui_elements:
            el.kill()
        self.ui_elements = []
        self.ui_element_actions = {}
        self.active_popup = None
        if self.layout:
            self.layout.destroy_all()
            self.layout = None

    # -------------------- Main Loop --------------------

    def handle_events(self):
        for event in pygame.event.get():
            
            event_consumed = self.gui_manager.process_events(event)


            


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
                if event.key == pygame.K_TAB:
                    if self.active_popup is None:
                        mods = pygame.key.get_mods()
                        reverse = mods & pygame.KMOD_SHIFT
                        ctrl = mods & pygame.KMOD_CTRL
                        
                        if self.is_text_input_active():
                            return  # don't steal Tab from the textbox
                    
                        if ctrl:
                            if self.layout:
                                self.layout.focus_next(reverse)
                        else:
                            if self.active_popup:
                                self.active_popup.focus_next(reverse)
                            elif self.state == "main_menu":
                                self.focus_next(reverse)
                            elif self.state == "workspace" and self.layout:
                                selected_view = self.layout.current_selected
                                if selected_view:
                                    selected_view.focus_next(reverse)

            
                if event.key == pygame.K_RETURN:
                    if self.active_popup:
                        self.active_popup.on_return()
                    else:
                        self.on_return()
            
            elif event.type == pygame.KEYUP and not event_consumed:
                if event.key == pygame.K_ESCAPE:
                    if self.active_popup:
                        self.active_popup.escape()
                    elif self.state == "main_menu":
                        QuitFromMenuPopup(self)
                    elif self.state == "workspace":
                        QuitFromGamePopup(self)

                       


    
            elif event.type == pygame_gui.UI_WINDOW_CLOSE: 
                if self.active_popup:
                    if event.ui_element == self.active_popup.window:
                        self.active_popup.cancel()

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element in self.ui_element_actions:
                    self.ui_element_actions[event.ui_element]()
                    

            
            
            if self.layout:
                self.layout.handle_event(event)
               
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.gui_manager.draw_ui(self.screen)
        
        if self.layout and self.active_popup is None:
            self.layout.draw(self.screen)

        
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
            
        if hasattr(self, 'client'):
            self.client.shutdown()
        pygame.quit()
        self.steamworks.unload()
        sys.exit()


if __name__ == "__main__":
    gui = ClientGUI()
    gui.run()