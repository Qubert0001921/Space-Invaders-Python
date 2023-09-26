import pygame
import game_config
from CollideBox import CollideBox
from Hittable import Hittable
import math


class Bullet(Hittable):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 12
        self.height = 50

        self.velocity = 700

        self.img = pygame.image.load(game_config.get_img_path("laser_beam.png"))
        self.img = pygame.transform.scale(self.img, (self.height, self.width))
        self.img = pygame.transform.rotate(self.img, 90)

        self.ch_height = 0.0
        self.ch_height_speed = 0.1

        self.collide_boxes = [
            CollideBox(self.x + 1, self.y + 1, self.width - 1, self.height - 2)
        ]

    def draw(self, display):
        if self.ch_height < 1:
            if self.ch_height + self.ch_height_speed > 1:
                self.ch_height = 1
            else:
                self.ch_height += self.ch_height_speed


        display.blit(pygame.transform.scale(self.img, (self.width, self.ch_height * self.height)), (self.x, self.y + self.height - (self.ch_height * self.height)))

        self.collide_boxes = [
            CollideBox(self.x + 1, self.y + 1, self.width - 1, self.height - 2)
        ]

        # for collideBox in self.collide_boxes:
        #     pygame.draw.rect(display, (255, 0, 0), collideBox.get_rect(), 1)
