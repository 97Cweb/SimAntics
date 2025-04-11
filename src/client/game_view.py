import pygame
import pygame_gui

from view import View

class GameView(View):
    def __init__(self, gui):
        super().__init__(gui, "Game")

    def set_container(self, panel):
        super().set_container(panel)
        label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((10, 10), (200, 30)),
            text="Game View",
            manager=self.gui.gui_manager,
            container=self.panel
        )
        self.elements.append(label)