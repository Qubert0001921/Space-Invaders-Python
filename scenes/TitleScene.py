import pygame
import random

from scenes.BaseScene import BaseScene


class TitleScene(BaseScene):
    def __init__(self, window, clock):
        super().__init__("Title", "TITLE", window, clock)
    
    def draw(self):
        super().draw()

    def handle_events(self, event):
        super().handle_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.scene_to_change = "Game"

    def mainloop(self):
        super().mainloop()


