import pygame
import pygame_gui

from focusable_group import FocusableGroup

DRAG_COLOR = (120, 120, 120)

class View(FocusableGroup):
    def __init__(self, gui, name):
        super().__init__()
        self.gui = gui
        self.name = name
        self.elements = []
        self.panel = None

    def set_container(self, panel):
        self.panel = panel

    def destroy(self):
        for el in self.elements:
            el.kill()
        self.elements.clear()
        if self.panel:
            self.panel.kill()
            self.panel = None

    def handle_event(self, event):
        pass

    def update(self, time_delta):
        pass
    
    def on_view_unfocused(self):
        if self.current_selected:
            if hasattr(self.current_selected, 'unselect'):
                self.current_selected.unselect()
            if hasattr(self.current_selected, 'unfocus'):
                self.current_selected.unfocus()

    def draw_drag_handles(self, surface):
        layout = getattr(self.gui, "layout", None)
        if layout:
            if layout.dragging_split:
                pygame.draw.rect(surface, DRAG_COLOR, layout.vertical_split_rect)
            if layout.dragging_file:
                pygame.draw.rect(surface, DRAG_COLOR, layout.file_split_rect)
            if layout.dragging_editor and hasattr(layout, "horizontal_split_rect"):
                pygame.draw.rect(surface, DRAG_COLOR, layout.horizontal_split_rect)

    def update_cursor(self, mouse_pos):
        layout = getattr(self.gui, "layout", None)
        if layout:
            if layout.vertical_split_rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
            elif layout.file_split_rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
            elif hasattr(layout, "horizontal_split_rect") and layout.horizontal_split_rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)