from pathlib import Path
import pygame
import pygame_gui


class FileBarView:
    def __init__(self, file_bar_panel: pygame_gui.elements.UIPanel, manager: pygame_gui.UIManager, save_path: str):
        self.file_bar_panel = file_bar_panel
        self.manager = manager
        self.root_path = Path(save_path)
        self.current_path = self.root_path
        self.scroll_panel = None
        self.file_buttons = []

        self.build_scroll_panel()
        self.refresh()

    def build_scroll_panel(self):
        
        if self.scroll_panel:
            self.scroll_panel.kill()

        self.scroll_panel = pygame_gui.elements.UIScrollingContainer(
            relative_rect=pygame.Rect((0, 0), (800, 100)),
            manager=self.manager,
            container=self.file_bar_panel,
            anchors={"left": "left", "right": "right", "top": "top", "bottom": "bottom"},
        )

    def refresh(self):
        for button, _, _ in self.file_buttons:
            button.kill()
        self.file_buttons.clear()
    
        folder_items = sorted([f for f in self.current_path.iterdir() if f.is_dir()], key=lambda x: x.name.lower())
        file_items = sorted([f for f in self.current_path.iterdir() if f.is_file()], key=lambda x: x.name.lower())
    
        all_items = []
    
        # Add up-button if not at root
        if self.current_path != self.root_path:
            all_items.append(("..", self.current_path.parent, True))  # Label, path, is_folder
    
        # Add folders and files
        all_items.extend([(item.name, item, item.is_dir()) for item in folder_items + file_items])
    
        item_width = 120
        item_height = 80
        padding = 10
        max_width = self.scroll_panel.get_container().get_size()[0]
        items_per_row = max(1, max_width // (item_width + padding))
    
        for index, (label, path, is_folder) in enumerate(all_items):
            row = index // items_per_row
            col = index % items_per_row
    
            x = col * (item_width + padding)
            y = row * (item_height + padding)
    
            button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((x, y), (item_width, item_height)),
                text=label,
                manager=self.manager,
                container=self.scroll_panel,
                tool_tip_text="Folder" if is_folder else "File"
            )
            self.file_buttons.append((button, path, is_folder))


    def handle_click(self, event):
        for button, path, is_folder in self.file_buttons:
            if event.ui_element == button:
                if is_folder:
                    self.current_path = path
                    self.refresh()
                else:
                    print(f"Clicked file: {path.name}")