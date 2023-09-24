from Hittable import Hittable
from Position import Position
from CollideBox import CollideBox
import colors
import pygame


class Slider(Hittable):
    def __init__(self, value, max_value, min_value, pos, width, height, color_bar, color_slider):
        super().__init__()
        self.value = value
        self.max_value = max_value
        self.min_value = min_value
        self.pos_bar = pos
        self.slider_width = 12
        self.slider_height = height * 2.6
        self.pos_slider = Position(self.pos_bar.x + (width-self.slider_width) * (self.value / self.max_value), self.pos_bar.y - (self.slider_height - height)//2)
        self.color_bar = color_bar
        self.color_slider = color_slider
        self.width = width
        self.height = height
        self.collide_boxes = [CollideBox(self.pos_bar.x, self.pos_bar.y-25, self.width, self.height+50)]

    def change_value(self, value):
        if self.min_value <= value <= self.max_value:
            self.value = value

        self.pos_slider = Position(self.pos_bar.x + (self.width-self.slider_width//2) * (self.value / self.max_value),
                                   self.pos_bar.y - (self.slider_height - self.height) // 2)


    def draw(self, surface):
        self.collide_boxes = [CollideBox(self.pos_bar.x -25, self.pos_bar.y-25, self.width+50, self.height+35)]

        pygame.draw.rect(surface, self.color_bar, (self.pos_bar.x, self.pos_bar.y, self.width, self.height))
        pygame.draw.rect(surface, self.color_slider, (self.pos_slider.x, self.pos_slider.y, self.slider_width, self.slider_height))
        # pygame.draw.rect(surface, colors.RED, self.collide_boxes[0].get_rect(), 2)
