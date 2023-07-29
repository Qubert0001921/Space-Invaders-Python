import pygame
from scenes.BaseScene import BaseScene
import game_config
from SpaceShip import SpaceShip
from Asteroid import Asteroid
from Bullet import Bullet
import math
import random


class GameScene(BaseScene):
    def __init__(self, window, clock):
        super().__init__("Game", "CAPTION", window, clock)
        self.bg_img = pygame.image.load(game_config.get_img_path("space.png"))
        self.bg_img = pygame.transform.scale(self.bg_img, (self.window.width, self.window.height))

        self.player = SpaceShip(80, 100, 100, self.window.height - 110)
        self.bullets = []
        self.asteroids = []

        self.time_to_asteroids = 5000
        self.elapsed_time = 0
        self.number_of_row = 1

        self.game_over = False

        self.font = pygame.font.SysFont("Arial", 20)

    def draw(self):
        super().draw()

        self.window.display.blit(self.bg_img, (0, 0))

        for asteroid in self.asteroids:
            asteroid.draw(self.window.display)
            asteroid.y += asteroid.velocity

        self.player.draw(self.window.display)

        self.player_movement()

        for bullet in self.bullets:
            bullet.draw(self.window.display)
            bullet.y -= bullet.velocity

            if bullet.y + bullet.height < 0 or bullet.y >= self.window.height:
                self.bullets.remove(bullet)

        if self.game_over:
            # TODO: HERE YOU ENDED LAST TIME
            # TODO: RENDER TEXT PROPERLY
            # TODO: FINISH GAME!!!
            self.font.render("GAME OVER", 1, (255, 255, 255))

    def player_movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.x -= self.player.velocity
        elif keys[pygame.K_RIGHT]:
            self.player.x += self.player.velocity
        if keys[pygame.K_UP]:
            self.player.y -= self.player.velocity
        elif keys[pygame.K_DOWN]:
            self.player.y += self.player.velocity

    def on_defeat(self):
        self.game_over = True

    def handle_events(self, event):
        super().handle_events(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.bullets.append(Bullet(self.player.x + self.player.width // 2 + 20, self.player.y - 6, 12, 50))
                self.bullets.append(Bullet(self.player.x + self.player.width // 2 - 33, self.player.y - 6, 12, 50))

    def mainloop(self):
        super().mainloop()

        self.elapsed_time += self.clock.tick(game_config.FPS)

        if self.elapsed_time >= self.time_to_asteroids:
            self.elapsed_time = 0
            self.time_to_asteroids = max(self.time_to_asteroids - 100, 200)
            self.number_of_row = min(self.number_of_row + 0.5, 10)

            for _ in range(math.floor(self.number_of_row)):
                self.asteroids.append(Asteroid(random.randint(0, self.window.width - 60), -60, 60, 60))
                # self.asteroids.append(Asteroid(200, -60, 60, 60))

        for asteroid in self.asteroids:
            for asteroid_collide_box in asteroid.collideBoxes:
                if asteroid_collide_box.check_if_collide(self.player.collideBoxes):
                    print("COLLIDE")
                    self.player.hit()
                    self.on_defeat()

