import os
import pygame
import pygame_gui

from file_bar_view import FileBarView

def create_main_menu_ui(gui):
    gui.clear_ui()
    gui.state = 'main_menu'

    gui.status_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 10), (300, 30)),
        text="Status: Disconnected",
        manager=gui.gui_manager,
    )
    gui.connect_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((10, 50), (150, 30)),
        text="Connect",
        manager=gui.gui_manager,
    )
    
    gui.ui_elements.extend([gui.status_label, gui.connect_button])
    gui.ui_element_actions[gui.connect_button] = gui.on_connect_clicked



def create_game_ui(gui):
    gui.clear_ui()
    gui.state = 'game'

    gui.game_area = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((0, 0), (800, 500)),
        manager=gui.gui_manager,
    )
    gui.file_bar = pygame_gui.elements.UIPanel(
        relative_rect=pygame.Rect((0, 500), (800, 100)),
        manager=gui.gui_manager,
    )


    # Create FileBarView instance (dynamically uses the client's save path)
    if gui.client and hasattr(gui.client, 'server_id'):
        save_folder = os.path.join("saves", gui.client.server_id)
        gui.file_bar_view = FileBarView(
            file_bar_panel=gui.file_bar,
            manager=gui.gui_manager,
            save_path=save_folder
        )
        gui.ui_elements.append(gui.file_bar_view.scroll_panel)


    gui.ui_elements.extend([gui.game_area, gui.file_bar])



def create_editor_ui(gui):
    gui.clear_ui()
    gui.state = 'editor'

    gui.editor_box = pygame_gui.elements.UITextBox(
        html_text="-- Lua code here",
        relative_rect=pygame.Rect((50, 50), (700, 400)),
        manager=gui.gui_manager,
    )
    gui.save_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((600, 470), (80, 30)),
        text="Save",
        manager=gui.gui_manager,
    )
    gui.return_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((690, 470), (80, 30)),
        text="Return",
        manager=gui.gui_manager,
    )

    gui.ui_elements.extend([gui.editor_box, gui.save_button, gui.return_button])
    gui.ui_element_actions[gui.save_button] = gui.on_save_clicked
    gui.ui_element_actions[gui.return_button] = gui.on_return_clicked


def create_quit_dialog(gui):
    if gui.quit_window is not None:
        return  # Already open

    gui.quit_context = gui.state
    gui.quit_window = pygame_gui.elements.UIWindow(
        rect=pygame.Rect((200, 200), (400, 200)),
        manager=gui.gui_manager,
        window_display_title="Quit"
    )

    label_text = (
        "Are you sure you want to quit?"
        if gui.state == "main_menu"
        else "Choose an action:"
    )
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((20, 20), (360, 30)),
        text=label_text,
        manager=gui.gui_manager,
        container=gui.quit_window
    )

    if gui.state == "main_menu":
        quit_confirm_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((60, 80), (120, 40)),
            text="Yes",
            manager=gui.gui_manager,
            container=gui.quit_window
        )
        quit_cancel_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((220, 80), (120, 40)),
            text="No",
            manager=gui.gui_manager,
            container=gui.quit_window
        )

        gui.ui_element_actions[quit_confirm_button] = gui.on_quit_os_clicked
        gui.ui_element_actions[quit_cancel_button] = gui.on_quit_cancel_clicked
    else:
        quit_os_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((20, 60), (160, 40)),
            text="Quit to OS",
            manager=gui.gui_manager,
            container=gui.quit_window
        )
        quit_main_menu_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((200, 60), (160, 40)),
            text="Quit to Main Menu",
            manager=gui.gui_manager,
            container=gui.quit_window
        )
        quit_cancel_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((110, 120), (160, 40)),
            text="Return",
            manager=gui.gui_manager,
            container=gui.quit_window
        )

        gui.ui_element_actions[quit_os_button] = gui.on_quit_os_clicked
        gui.ui_element_actions[quit_main_menu_button] = gui.on_quit_main_menu_clicked
        gui.ui_element_actions[quit_cancel_button] = gui.on_quit_cancel_clicked


def close_quit_popup(gui):
    if gui.quit_window is not None and gui.quit_window.alive():
        gui.quit_window.kill()
    gui.quit_window = None


def popup_active(gui):
    return (gui.quit_window and gui.quit_window.alive()) or (gui.connect_window and gui.connect_window.alive())



def create_connect_dialog(gui):
    if gui.connect_window is not None:
        return  # Already open

    gui.connect_window = pygame_gui.elements.UIWindow(
        rect=pygame.Rect((250, 150), (300, 250)),
        manager=gui.gui_manager,
        window_display_title="Connect to Server"
    )

    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 10), (280, 30)),
        text="Password:",
        manager=gui.gui_manager,
        container=gui.connect_window
    )
    gui.connect_password_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((10, 40), (280, 30)),
        manager=gui.gui_manager,
        container=gui.connect_window
    )
    gui.connect_password_input.set_text("")
    gui.connect_password_input.set_text_hidden(True)
    gui.connect_password_input.focus()

    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 80), (280, 30)),
        text="IP Address:",
        manager=gui.gui_manager,
        container=gui.connect_window
    )
    gui.connect_ip_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((10, 110), (280, 30)),
        manager=gui.gui_manager,
        container=gui.connect_window
    )
    gui.connect_ip_input.set_text("127.0.0.1")

    # TCP Port
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 150), (130, 30)),
        text="TCP Port:",
        manager=gui.gui_manager,
        container=gui.connect_window
    )
    gui.connect_tcp_port_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((110, 150), (70, 30)),
        manager=gui.gui_manager,
        container=gui.connect_window
    )
    gui.connect_tcp_port_input.set_text("65432")
    
    # UDP Port
    pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((10, 185), (130, 30)),
        text="UDP Port:",
        manager=gui.gui_manager,
        container=gui.connect_window
    )
    gui.connect_udp_port_input = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((110, 185), (70, 30)),
        manager=gui.gui_manager,
        container=gui.connect_window
    )
    gui.connect_udp_port_input.set_text("65433")
    
    # Join Button
    gui.connect_submit_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((200, 185), (80, 30)),
        text="Join",
        manager=gui.gui_manager,
        container=gui.connect_window
    )


    gui.ui_element_actions[gui.connect_submit_button] = gui.on_connect_submit

