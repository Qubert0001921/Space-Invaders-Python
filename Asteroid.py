import pygame
import game_config
from CollideBox import CollideBox
from Hittable import Hittable
from Animationable import Animationable
import random
import math


class Asteroid(Hittable, Animationable):
    def __init__(self, x, y, width, height):
        super().__init__(animation_speed=0.3, frame_idle=pygame.image.load(game_config.get_img_path("asteroid_idle.png")), frame_idle_size=(width, height))

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = random.randrange(500, game_config.MAX_ASTEROID_VELOCITY)
        self.collide_boxes = [CollideBox(self.x + 5, self.y + 7, self.width // 2, self.height // 2),
                             CollideBox(self.x + self.width // 2 - 8, self.y + self.height // 2 - 2, self.width // 2,
                                        self.height // 2)]

        self.load_animation(game_config.get_frames("asteroid_destroy", "asteroid_"), (self.width*2, self.height*2))

    def on_animation_end(self):
        super().on_animation_end()
        self.show = False

    def draw(self, display):
        frame = self.animation()

        if frame is not None:
            pos = (self.x, self.y)
            if frame.get_width() != self.width:
                pos = (self.x - frame.get_width()//4, self.y - frame.get_height()//4)
            display.blit(frame, pos)

        if self.hittable:
            self.collide_boxes = [CollideBox(self.x + 5, self.y + 7, self.width // 2, self.height // 2),
                                 CollideBox(self.x + self.width // 2 - 8, self.y + self.height // 2 - 2, self.width // 2,
                                            self.height // 2)]
        else:
            self.collide_boxes = []
        # for collideBox in self.collideBoxes:
        #     pygame.draw.rect(display, (255, 0, 0), collideBox.get_rect(), 2)
