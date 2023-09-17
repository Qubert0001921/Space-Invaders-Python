import pygame
import game_config
from CollideBox import CollideBox
from Hittable import Hittable
import random


class SpaceShip(Hittable):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.velocity = 500
        self.collide_boxes = [CollideBox(self.x + self.width // 4 + 5, self.y + 5, 30, self.height // 2 - 5),
                                CollideBox(self.x + 5, self.y + self.height // 2, self.width - 10, self.height // 2)]
        self.img = pygame.image.load(game_config.get_img_path("spaceship.png"))
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.immunity_max = 5
        self.immunity = self.immunity_max
    def decrement_immunity(self, asteroid_velocity):
        self.immunity -= asteroid_velocity / game_config.MAX_ASTEROID_VELOCITY
        if self.immunity < 0:
            self.immunity = 0
        self.velocity -= asteroid_velocity * 0.15

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))
        self.collide_boxes = [CollideBox(self.x + self.width // 4 + 5, self.y + 5, 30, self.height // 2 - 5),
                                CollideBox(self.x + 5, self.y + self.height // 2, self.width - 10, self.height // 2)]
        # for collideBox in self.collideBoxes:
        #     pygame.draw.rect(display, (255, 0, 0), collideBox.get_rect(), 2)

