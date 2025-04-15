import pygame
import pygame_gui

from escapable_popup import EscapablePopup

class QuitFromGamePopup(EscapablePopup):
    def setup_ui(self):
        self.make_popup_window()
        width, height = self.size

        self.menu_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((width // 2 - 50, height - 160), (100, 40)),
            text="Quit to Main Menu",
            manager=self.gui.gui_manager,
            container=self.window
        )
        
        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((width // 2 - 50, height - 110), (100, 40)),
            text="Quit to OS",
            manager=self.gui.gui_manager,
            container=self.window
        )
        self.gui.ui_element_actions[self.quit_button] = self.quit_to_os
        self.gui.ui_element_actions[self.menu_button] = self.quit_to_menu

        self.focus_order = [self.default_button, self.menu_button, self.quit_button]
        self.default_focus_index = 0
        self.focus_default_element()
        
    def quit_to_menu(self):
        self.cancel()
        self.gui.client.shutdown()
        self.gui.init_main_menu()
        

    def quit_to_os(self):
        self.cancel()
        self.gui.quit()
        

    def on_return_default(self):
        self.cancel()
        

