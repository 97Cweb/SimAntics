import pygame
import pygame_gui

from view import View

class EditorView(View):
    def __init__(self, gui):
        super().__init__(gui, "Editor")
        self.textbox = None

    def set_container(self, panel):
        super().set_container(panel)
        self.textbox = pygame_gui.elements.UITextEntryBox(
            initial_text="-- Lua code here",
            relative_rect=pygame.Rect((10, 10), (panel.get_container().get_size()[0] - 20, panel.get_container().get_size()[1] - 20)),
            manager=self.gui.gui_manager,
            container=self.panel
        )
        self.elements.append(self.textbox)