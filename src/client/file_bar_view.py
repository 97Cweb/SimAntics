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
        self.rename_window = None
        self.rename_entry = None
        self.rename_target = None
        self.creation_mode = None  # 'file' or 'folder'
        
        self.confirmation_window = None
        self.confirmation_ok_button = None
        self.confirmation_cancel_button = None
        
        self.upload_callback = None



        
        self.file_buttons = []

        self.build_scroll_panel()
        
        self.upload_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((680, 0), (120, 30)),
            text="Upload",
            manager=self.manager,
            container=self.file_bar_panel
        )
        
        self.create_file_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((680, 30), (120, 30)),
            text="New File",
            manager=self.manager,
            container=self.file_bar_panel
        )
        
        self.create_folder_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((680, 60), (120, 30)),
            text="New Folder",
            manager=self.manager,
            container=self.file_bar_panel
        )

        
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
        for button, _, _, rename_button, delete_button in self.file_buttons:
            button.kill()
            if rename_button:
                rename_button.kill()
            if delete_button:
                delete_button.kill()
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
    
            button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((x, y), (item_width, item_height)),
                text=label,
                manager=self.manager,
                container=self.scroll_panel,
                tool_tip_text="Folder" if is_folder else "File"
            )
            
            rename_button = None
            delete_button = None
            if label != "..":
                # Small Rename (I) button
                rename_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect((x + item_width - 40, y + 5), (15, 15)),
                    text="I",
                    manager=self.manager,
                    container=self.scroll_panel,
                    tool_tip_text="Rename"
                )
        
                # Small Delete (X) button
                delete_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect((x + item_width - 20, y + 5), (15, 15)),
                    text="X",
                    manager=self.manager,
                    container=self.scroll_panel,
                    tool_tip_text="Delete"
                )
    
            self.file_buttons.append((button, path, is_folder, rename_button, delete_button))




    def handle_event(self, event):
        # Confirmation popup handling
        if self.confirmation_window:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._cancel_confirmation()
                elif event.key == pygame.K_RETURN:
                    full_path = self.current_path / self.rename_entry.get_text().strip()
                    self._execute_rename_or_create(full_path)
                return
    
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.confirmation_ok_button:
                    full_path = self.current_path / self.rename_entry.get_text().strip()
                    self._execute_rename_or_create(full_path)
                elif event.ui_element == self.confirmation_cancel_button:
                    self._cancel_confirmation()
                return
    
        # Rename popup handling
        if self.rename_window:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._cancel_rename()
                return
    
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_element == self.rename_entry:
                self._apply_rename()
                return
    
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.rename_ok_button:
                    self._apply_rename()
                    return
                elif event.ui_element == self.rename_cancel_button:
                    self._cancel_rename()
                    return
    
        # New file/folder buttons
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.create_file_button:
                self.creation_mode = "file"
                self.show_name_entry_popup("Create New File", "new_file.txt")
                return
            elif event.ui_element == self.create_folder_button:
                self.creation_mode = "folder"
                self.show_name_entry_popup("Create New Folder", "New Folder")
                return
            
            elif event.ui_element == self.upload_button:
                if self.upload_callback:
                    self.upload_callback()

    
            # File/folder buttons (main bar)
            for button, path, is_folder, rename_btn, delete_btn in self.file_buttons:
                if event.ui_element == button:
                    if is_folder:
                        self.current_path = path
                        self.refresh()
                    else:
                        print(f"Clicked file: {path.name}")
                    return
                elif event.ui_element == rename_btn:
                    self.rename_selected(path)
                    return
                elif event.ui_element == delete_btn:
                    self.delete_selected(path)
                    return


    def show_name_entry_popup(self, title: str, default_text: str = ""):
        if self.rename_window:
            return
    
        self.rename_window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect((300, 200), (300, 150)),
            manager=self.manager,
            window_display_title=title,
        )
    
        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((10, 10), (280, 30)),
            text=title,
            manager=self.manager,
            container=self.rename_window,
        )
    
        self.rename_entry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((10, 50), (280, 30)),
            manager=self.manager,
            container=self.rename_window,
        )
        self.rename_entry.set_text(default_text)
        self.rename_entry.focus()
        self.rename_entry.select_range = [0, len(default_text)]
    
        self.rename_ok_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((30, 100), (100, 30)),
            text="OK",
            manager=self.manager,
            container=self.rename_window,
        )
    
        self.rename_cancel_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((170, 100), (100, 30)),
            text="Cancel",
            manager=self.manager,
            container=self.rename_window,
        )

        
    def _apply_rename(self):
        new_name = self.rename_entry.get_text().strip()
        if not new_name:
            return
    
        full_path = self.current_path / new_name
        if full_path.exists() and not self.confirmation_window:
            self._show_overwrite_confirmation(full_path)
            return
    
        self._execute_rename_or_create(full_path)

    def _execute_rename_or_create(self, full_path):
        try:
            if self.creation_mode == "file":
                full_path.touch(exist_ok=True)
            elif self.creation_mode == "folder":
                full_path.mkdir(exist_ok=True)
            elif self.rename_target:
                new_path = self.rename_target.with_name(full_path.name)
                self.rename_target.rename(new_path)
        except Exception as e:
            print(f"Operation failed: {e}")
    
        self._cancel_confirmation()
        self._cancel_rename()
        self.refresh()

    
    def _cancel_rename(self):
        if self.rename_window:
            self.rename_window.kill()
            self.rename_window = None
            self.rename_entry = None
            self.rename_target = None
            self.creation_mode = None
            
    def _cancel_confirmation(self):
        if self.confirmation_window:
            self.confirmation_window.kill()
            self.confirmation_window = None
            self.confirmation_ok_button = None
            self.confirmation_cancel_button = None



    def rename_selected(self, path: Path):
        self.rename_target = path
        self.creation_mode = None  # Ensure it's not in creation mode
        self.show_name_entry_popup(f"Rename '{path.name}' to:", path.name)


    def delete_selected(self, path):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            import shutil
            shutil.rmtree(path)
        self.refresh()


    def _show_overwrite_confirmation(self, full_path: Path):
        self.confirmation_window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect((350, 250), (300, 120)),
            manager=self.manager,
            window_display_title="Confirm Overwrite",
        )
    
        pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((10, 10), (280, 30)),
            text=f"'{full_path.name}' exists. Overwrite?",
            manager=self.manager,
            container=self.confirmation_window,
        )
    
        self.confirmation_ok_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((30, 60), (100, 30)),
            text="Overwrite",
            manager=self.manager,
            container=self.confirmation_window,
        )
    
        self.confirmation_cancel_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((170, 60), (100, 30)),
            text="Cancel",
            manager=self.manager,
            container=self.confirmation_window,
        )




