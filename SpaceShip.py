import pygame
import game_config
from CollideBox import CollideBox


class SpaceShip(object):
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.velocity = 5
        self.collideBoxes = [CollideBox(self.x + self.width // 4 + 5, self.y + 5, 30, self.height // 2 - 5),
                             CollideBox(self.x + 5, self.y + self.height // 2, self.width - 10, self.height // 2)]
        self.img = pygame.image.load(game_config.get_img_path("spaceship.png"))
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

    def hit(self):
        print("Hit")

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))
        self.collideBoxes = [CollideBox(self.x + self.width // 4 + 5, self.y + 5, 30, self.height // 2 - 5),
                             CollideBox(self.x + 5, self.y + self.height // 2, self.width - 10, self.height // 2)]
        for collideBox in self.collideBoxes:
            pygame.draw.rect(display, (255, 0, 0), collideBox.get_rect(), 2)

