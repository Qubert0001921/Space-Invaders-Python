import pygame
import game_config


class Bullet(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.velocity = 8

        self.img = pygame.image.load(game_config.get_img_path("laser_beam.png"))
        self.img = pygame.transform.scale(self.img, (self.height, self.width))
        self.img = pygame.transform.rotate(self.img, 90)

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))
