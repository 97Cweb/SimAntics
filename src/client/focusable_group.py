class FocusableGroup:
    def __init__(self, default_focus_index=0):
        self.focus_order = []
        self.current_selected = None
        self.default_focus_index = default_focus_index

    def set_selected(self, element):
        # Deselect previous element
        if self.current_selected:
            if hasattr(self.current_selected, 'unselect'):
                self.current_selected.unselect()
            if hasattr(self.current_selected, 'unfocus'):
                self.current_selected.unfocus()

        self.current_selected = element

        if hasattr(element, 'select'):
            element.select()
        if hasattr(element, 'focus'):
            element.focus()

    def focus_next(self, reverse=False):
        if not self.focus_order:
            return

        current = None
        for i, el in enumerate(self.focus_order):
            if el == self.current_selected:
                current = i
                break

        next_index = 0 if current is None else (
            (current - 1) if reverse else (current + 1)
        ) % len(self.focus_order)

        self.set_selected(self.focus_order[next_index])

    def focus_default_element(self):
        if self.focus_order and 0 <= self.default_focus_index < len(self.focus_order):
            self.set_selected(self.focus_order[self.default_focus_index])
        elif self.focus_order:
            self.set_selected(self.focus_order[0])

    def on_return(self):
        if isinstance(self.current_selected, object) and hasattr(self.current_selected, 'select'):
            import pygame
            import pygame_gui
            event = pygame.event.Event(pygame_gui.UI_BUTTON_PRESSED, {"ui_element": self.current_selected})
            pygame.event.post(event)
        elif hasattr(self, 'on_return_default'):
            self.on_return_default()
