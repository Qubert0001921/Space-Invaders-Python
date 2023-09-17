import pygame
import game_config
from CollideBox import CollideBox
from Hittable import Hittable


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

        self.collide_boxes = [
            CollideBox(self.x + 1, self.y + 1, self.width - 1, self.height - 2)
        ]

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))

        self.collide_boxes = [
            CollideBox(self.x + 1, self.y + 1, self.width - 1, self.height - 2)
        ]

        # for collideBox in self.collide_boxes:
        #     pygame.draw.rect(display, (255, 0, 0), collideBox.get_rect(), 1)
