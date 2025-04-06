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
        self.context_menu = None
        self.context_menu_target = None
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
        # Clear previous buttons
        for entry in self.file_buttons:
            entry['main'].kill()
            entry['action'].kill()
        self.file_buttons.clear()
    
        folder_items = sorted([f for f in self.current_path.iterdir() if f.is_dir()], key=lambda x: x.name.lower())
        file_items = sorted([f for f in self.current_path.iterdir() if f.is_file()], key=lambda x: x.name.lower())
    
        all_items = []
    
        if self.current_path != self.root_path:
            all_items.append(("..", self.current_path.parent, True))
    
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
    
            main_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((x, y), (item_width, item_height)),
                text=label,
                manager=self.manager,
                container=self.scroll_panel,
                tool_tip_text="Folder" if is_folder else "File"
            )
    
            action_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((x + item_width - 24, y + 4), (20, 20)),
                text="⋮",
                manager=self.manager,
                container=self.scroll_panel,
                tool_tip_text="Actions"
            )
    
            self.file_buttons.append({
                'main': main_button,
                'action': action_button,
                'path': path,
                'is_folder': is_folder
            })
    
        if self.context_menu:
            self.context_menu.kill()
            self.context_menu = None
            self.context_menu_target = None




    def handle_click(self, event):
        for file_info in self.file_buttons:
            path = file_info['path']
            is_folder = file_info['is_folder']
    
            if event.ui_element == file_info['main']:
                if is_folder:
                    self.current_path = path
                    self.refresh()
                else:
                    print(f"Clicked file: {path.name}")
                return
    
            elif event.ui_element == file_info['action']:
                # Kill previous menu
                if self.context_menu:
                    self.context_menu.kill()
    
                self.context_menu_target = path
                self.context_menu = pygame_gui.elements.UIDropDownMenu(
                    options_list=["Rename", "Delete"],
                    starting_option="Choose...",
                    relative_rect=pygame.Rect(event.ui_element.rect.bottomleft, (100, 30)),
                    manager=self.manager,
                    container=self.file_bar_panel
                )
                return



    
    def handle_context_action(self, event):
        if not self.context_menu or not self.context_menu_target:
            return
    
        path = self.context_menu_target
    
        if event.text == "Rename":
            new_name = input(f"Rename '{path.name}' to: ")
            if new_name:
                new_path = path.with_name(new_name)
                path.rename(new_path)
    
        elif event.text == "Delete":
            confirm = input(f"Delete '{path.name}'? (y/n): ").lower()
            if confirm == 'y':
                if path.is_file():
                    path.unlink()
                elif path.is_dir():
                    import shutil
                    shutil.rmtree(path)
    
        self.context_menu.kill()
        self.context_menu = None
        self.context_menu_target = None
        self.refresh()


