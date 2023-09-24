from Hittable import Hittable
from CollideBox import CollideBox
from Renderable import Renderable
import pygame


class Label(Renderable):
    def __init__(self, pos, font, text, text_color, antialias=False, hittable=False):
        self.text = font.render(text, int(antialias), text_color)
        super().__init__(self.text.get_width(), self.text.get_height(), pos)

        self.font = font
        self.antialias = antialias
        self.content = text
        self.text_color = text_color

        if hittable:
            self.refresh_collide_box()

    def change_color(self, color):
        self.text = self.font.render(self.content, int(self.antialias), color)

    def refresh_collide_box(self):
        self.collide_boxes = [CollideBox(self.pos.x, self.pos.y, self.text.get_width(), self.text.get_height())]

    def change_text(self, content):
        self.text = self.font.render(content, int(self.antialias), self.text_color)
        self.content = content
        self.refresh_collide_box()
        self.width = self.text.get_width()
        self.height = self.text.get_height()

    def draw(self, surface):
        surface.blit(self.text, self.pos.to_tuple())
        self.refresh_collide_box()


