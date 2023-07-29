import pygame
import game_config
from CollideBox import CollideBox


class Asteroid(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.collideBoxes = [CollideBox(self.x + 5, self.y + 7, self.width // 2, self.height // 2),
                             CollideBox(self.x + self.width // 2 - 8, self.y + self.height // 2 - 2, self.width // 2,
                                        self.height // 2)]

        self.img = pygame.image.load(game_config.get_img_path("asteroid.png"))
        self.img = pygame.transform.scale(self.img, (self.height, self.width))

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))
        self.collideBoxes = [CollideBox(self.x + 5, self.y + 7, self.width // 2, self.height // 2),
                             CollideBox(self.x + self.width // 2 - 8, self.y + self.height // 2 - 2, self.width // 2,
                                        self.height // 2)]
        # for collideBox in self.collideBoxes:
        #     pygame.draw.rect(display, (255, 0, 0), collideBox.get_rect(), 2)
