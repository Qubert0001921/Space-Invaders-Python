import pygame
import game_config


class Asteroid(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5

        self.img = pygame.image.load(game_config.get_img_path("asteroid.png"))
        self.img = pygame.transform.scale(self.img, (self.height, self.width))

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))
