import pygame
import pygame_gui

from escapable_popup import EscapablePopup

class QuitFromMenuPopup(EscapablePopup):
    def setup_ui(self):
        super().setup_ui()
        width, height = self.size

        quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((width // 2 - 50, height - 110), (100, 40)),
            text="Quit to OS",
            manager=self.gui.gui_manager,
            container=self.window
        )

        self.gui.ui_element_actions[quit_button] = self.quit_to_os

    def quit_to_os(self):
        self.gui.quit()
        self.cancel()