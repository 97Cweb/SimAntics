import pygame
import pygame_gui

from typing import override

from game_view import GameView
from editor_view import EditorView
from file_explorer_view import FileExplorerView
from focusable_group import FocusableGroup

class LayoutManager(FocusableGroup):
    def __init__(self, gui):
        super().__init__()
        self.gui = gui
        self.views = {}
        self.panels = []
        self.ratio_split = 0.5
        self.editor_ratio = 0.5
        self.file_ratio = 0.5
        self.dragging_split = False
        self.dragging_editor = False
        self.dragging_file = False
        self.min_split = 0.0
        self.max_split = 1.0
        self.create_default_layout()
        
        self.default_focus_index = 0
        self.focus_default_element()
        self.drop_focus()
        
        print(self.views)
        for view in self.views.values():
            view.drop_focus()
        
        self.views["game"].take_focus()
        
        self.highlight_color = pygame.Color('#7289da')
        self.highlight_thickness = 3


    def create_default_layout(self):
        self.destroy_all()
        width, height = self.gui.screen.get_size()

        left_width = int(width * self.ratio_split)
        right_width = width - left_width
        game_height = int((height) * self.file_ratio)

        self.vertical_split_rect = pygame.Rect((left_width - 2, 0), (4, height))
        self.file_split_rect = pygame.Rect((0,  game_height - 2), (left_width, 4))

        game_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((0, 0), (left_width, game_height)),
            manager=self.gui.gui_manager)

        if self.file_ratio < 0.8:
            file_panel = pygame_gui.elements.UIPanel(
                relative_rect=pygame.Rect((0, game_height), (width, height - game_height)),
                manager=self.gui.gui_manager)
            editor_panel = pygame_gui.elements.UIPanel(
                relative_rect=pygame.Rect((left_width, 0), (right_width, game_height)),
                manager=self.gui.gui_manager)
        else:
            editor_height = int((height) * self.editor_ratio)
            explorer_height = (height) - editor_height
            editor_panel = pygame_gui.elements.UIPanel(
                relative_rect=pygame.Rect((left_width, 0), (right_width, editor_height)),
                manager=self.gui.gui_manager)
            file_panel = pygame_gui.elements.UIPanel(
                relative_rect=pygame.Rect((left_width, editor_height), (right_width, explorer_height)),
                manager=self.gui.gui_manager)
            self.horizontal_split_rect = pygame.Rect((left_width, editor_height - 2), (right_width, 4))

        self.panels.extend([game_panel, editor_panel, file_panel])

        self.views['game'] = GameView(self.gui)
        self.views['editor'] = EditorView(self.gui)
        self.views['explorer'] = FileExplorerView(self.gui)

        self.views['game'].set_container(game_panel)
        self.views['editor'].set_container(editor_panel)
        self.views['explorer'].set_container(file_panel)
        
        self.focus_order = [
            self.views['game'],
            self.views['editor'],
            self.views['explorer']
        ]
        

        
        

    def handle_event(self, event):
        
        if self.current_selected and hasattr(self.current_selected, "handle_event"):
            self.current_selected.handle_event(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.vertical_split_rect.collidepoint(event.pos):
                self.dragging_split = True
            if hasattr(self, 'horizontal_split_rect') and self.horizontal_split_rect.collidepoint(event.pos):
                self.dragging_editor = True
            if self.file_split_rect.collidepoint(event.pos):
                self.dragging_file = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging_split = False
            self.dragging_editor = False
            self.dragging_file = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging_split:
                ratio = event.pos[0] / self.gui.screen.get_width()
                self.ratio_split = max(self.min_split, min(self.max_split, ratio))
                self.on_resize()
            elif self.dragging_editor:
                h = self.gui.screen.get_height() - 30
                ratio = (event.pos[1] - 30) / h
                self.editor_ratio = max(self.min_split, min(self.max_split, ratio))
                self.on_resize()
            elif self.dragging_file:
                h = self.gui.screen.get_height() - 30
                ratio = (event.pos[1] - 30) / h
                self.file_ratio = max(self.min_split, min(self.max_split, ratio))
                self.on_resize()

    def destroy_all(self):
        for view in self.views.values():
            view.destroy()
        for panel in self.panels:
            panel.kill()
        self.views.clear()
        self.panels.clear()


    def on_resize(self):
        if self.gui.state != "workspace":
            return
        self.destroy_all()
        self.create_default_layout()
    

        
    def draw(self, surface):
        if self.current_selected and hasattr(self.current_selected, 'panel'):
            panel = self.current_selected.panel
            rect = panel.get_abs_rect()
            pygame.draw.rect(surface, self.highlight_color, rect, self.highlight_thickness)

