import pygame
import game_config


class BaseScene(object):
    def __init__(self, name, caption, window, clock):
        self.caption = caption
        self.window = window
        self.clock = clock
        self.name = name
        self.scene_to_change = name
        self.deltatime = 0

    def draw(self):
        pygame.display.set_caption(self.caption)

    def mainloop(self, deltatime):
        pass

    def handle_events(self, event):
        pass

    def init(self):
        pass
