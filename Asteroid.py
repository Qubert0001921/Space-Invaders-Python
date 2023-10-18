import pygame
import game_config
from CollideBox import CollideBox
from Hittable import Hittable
from Animationable import Animationable
import random
import math


class Asteroid(Hittable):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = random.randrange(500, game_config.MAX_ASTEROID_VELOCITY)
        self.collide_boxes = [CollideBox(self.x + 5, self.y + 7, self.width // 2, self.height // 2),
                             CollideBox(self.x + self.width // 2 - 8, self.y + self.height // 2 - 2, self.width // 2,
                                        self.height // 2)]

        self.destroy_animation = game_config.get_frames("asteroid_destroy", "asteroid_")
        self.destroy_animation = [pygame.transform.scale(x, (self.width*2, self.height*2)) for x in self.destroy_animation]
        self.animations = [
            self.destroy_animation
        ]

        self.current_animation = 0
        self.current_frame_index = 0
        self.animate = False
        self.show = True
        self.animation_speed = 0.3

        self.frame_idle = pygame.image.load(game_config.get_img_path("asteroid_idle.png"))
        self.frame_idle = pygame.transform.scale(self.frame_idle, (self.width, self.height))

    def on_animation_end(self):
        super().on_animation_end()
        self.show = False

    def draw(self, display):
        # frame = self.animation()
        #
        # if frame is not None:
        #     pos = (self.x, self.y)
        #     if frame.get_width() != self.width:
        #         pos = (self.x - frame.get_width()//4, self.y - frame.get_height()//4)
        #     display.blit(frame, pos)

        if self.show:
            if self.animate:
                frame = self.animations[self.current_animation][math.floor(self.current_frame_index)]
                display.blit(frame, (self.x - frame.get_width()//4, self.y - frame.get_height()//4))

                self.current_frame_index += self.animation_speed
                if self.current_frame_index > len(self.animations[self.current_animation]):
                    self.show = False
            else:
                display.blit(self.frame_idle, (self.x, self.y))

        if self.hittable:
            self.collide_boxes = [CollideBox(self.x + 5, self.y + 7, self.width // 2, self.height // 2),
                                 CollideBox(self.x + self.width // 2 - 8, self.y + self.height // 2 - 2, self.width // 2,
                                            self.height // 2)]
        else:
            self.collide_boxes = []
        # for collideBox in self.collideBoxes:
        #     pygame.draw.rect(display, (255, 0, 0), collideBox.get_rect(), 2)
