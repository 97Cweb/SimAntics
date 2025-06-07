from pygame_gui.elements import UITextEntryBox
import pygame


class TabFriendlyTextBox(UITextEntryBox):
    def process_event(self, event: pygame.event.Event) -> bool:

        # Add tab support manually
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB and self.is_focused:
            # Insert a tab character manually at the cursor
            self.set_text(self.get_text() + "    ")  # 4 spaces instead of actual tab character
            return True  # Mark event as handled
        
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE and self.is_focused:
            self.unfocus()
            return True  # consume Escape
        
        return super().process_event(event)