import pygame
import game_config
from CollideBox import CollideBox
from Hittable import Hittable
import math
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

        self.frames_running = game_config.get_frames("spaceship_running", "spaceship_running_")
        self.frames_running = [pygame.transform.scale(x, (self.width, self.height)) for x in self.frames_running]

        self.frames_starting = game_config.get_frames("spaceship_start", "spaceship_start_")
        self.frames_starting = [pygame.transform.scale(x, (self.width, self.height)) for x in self.frames_starting]

        self.frames_explosion = game_config.get_frames("ship_explosion", "Ship_explosion_")
        self.frames_explosion = [pygame.transform.scale(x, (self.height, self.height)) for x in self.frames_explosion]

        self.frame_idle = self.frames_starting[0]

        self.show = True

        self.animations = [
            self.frames_starting,
            self.frames_running,
            self.frames_explosion
        ]
        self.current_frame = 0
        self.animation_speed = 0.2
        self.current_animation = 0

        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.immunity_max = 5
        self.immunity = self.immunity_max
        # self.immunity = 0.1

    def decrement_immunity(self, asteroid_velocity):
        self.immunity -= asteroid_velocity / game_config.MAX_ASTEROID_VELOCITY
        if self.immunity < 0:
            self.immunity = 0
        self.velocity -= asteroid_velocity * 0.15

    def draw(self, display):
        if self.show:
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.animations[self.current_animation]) - 1:
                self.current_frame = 0

                if self.current_animation == 0:
                    self.current_animation = 1

                if self.current_animation == 2:
                    self.show = False

            display.blit(self.animations[self.current_animation][math.floor(self.current_frame)], (self.x, self.y))

        self.collide_boxes = [CollideBox(self.x + self.width // 4 + 5, self.y + 5, 30, self.height // 2 - 5),
                              CollideBox(self.x + 5, self.y + self.height // 2, self.width - 10, self.height // 2)]
        # for collideBox in self.collideBoxes:
        #     pygame.draw.rect(display, (255, 0, 0), collideBox.get_rect(), 2)

