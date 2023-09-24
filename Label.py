from Hittable import Hittable
from CollideBox import CollideBox
import pygame


class Label(Hittable):
    def __init__(self, pos, font, text, text_color, antialias=False, hittable=False):
        super().__init__()
        self.font = font
        self.antialias = antialias
        self.text = font.render(text, int(antialias), text_color)
        self.content = text
        self.text_color = text_color
        self.pos = pos
        if hittable:
            self.add_collide_box(CollideBox(pos.x, pos.y, self.text.get_width(), self.text.get_height()))

    def change_color(self, color):
        self.text = self.font.render(self.content, int(self.antialias), color)

    def draw(self, surface):
        surface.blit(self.text, self.pos.to_tuple())


