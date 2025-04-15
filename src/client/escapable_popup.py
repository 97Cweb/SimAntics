import pygame
import pygame_gui
from abc import ABC, abstractmethod
from focusable_group import FocusableGroup

class EscapablePopup(FocusableGroup, ABC):
    def __init__(self, gui, title="Popup", size=(300, 200)):
        super().__init__()
        self.gui = gui
        self.title = title
        self.size = size
        self.window = None
        self.focus_order = []
        self.default_button = None
        
    
            
        self.gui.active_popup = self
        self.setup_ui()

    @abstractmethod
    def setup_ui(self):
        pass

    def make_popup_window(self):
        width, height = self.size
        x = (self.gui.screen.get_width() - width) // 2
        y = (self.gui.screen.get_height() - height) // 2

        self.window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect(x, y, width, height),
            window_display_title=self.title,
            manager=self.gui.gui_manager
        )

        self.default_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((width // 2 - 50, height - 60), (100, 40)),
            text="Cancel",
            manager=self.gui.gui_manager,
            container=self.window
        )
        self.gui.ui_element_actions[self.default_button] = self.cancel

    def escape(self):
        self.cancel()

    def cancel(self):
        if self.window:
            self.window.kill()
            self.window = None
        if hasattr(self.gui, "active_popup"):
            self.gui.active_popup = None



    
