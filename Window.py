import pygame
import game_config
from SpaceShip import SpaceShip
from Bullet import Bullet
from Asteroid import Asteroid
import random
import math


class Window(object):
    def __init__(self, width, height, caption):
        pygame.init()
        pygame.font.init()

        self.width = width
        self.height = height
        self.caption = caption
        self.display = pygame.display.set_mode((self.width, self.height))

        self.bg_img = pygame.image.load(game_config.get_img_path("space.png"))
        self.bg_img = pygame.transform.scale(self.bg_img, (self.width, self.height))

        self.player = SpaceShip(80, 100, 100, self.height - 110)
        self.bullets = []
        self.asteroids = []

        self.clock = pygame.time.Clock()

        pygame.display.set_caption(self.caption)

    def draw(self):
        self.display.blit(self.bg_img, (0, 0))

        # for asteroid in self.asteroids:
        #     asteroid.draw(self.display)
        #     asteroid.y += asteroid.velocity
        for a in self.asteroids:
            a.draw(self.display)

        self.player.draw(self.display)

        self.player_movement()

        for bullet in self.bullets:
            bullet.draw(self.display)
            bullet.y -= bullet.velocity

            if bullet.y + bullet.height < 0 or bullet.y >= self.height:
                self.bullets.remove(bullet)


        # print(len(self.bullets))
        pygame.display.update()

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

    def mainloop(self):
        run = True

        time_to_asteroids = 4000
        elapsed_time = 0
        number_of_row = 1

        self.asteroids.append(Asteroid(200, 400, 60, 60))

        while run:
            elapsed_time += self.clock.tick(game_config.FPS)

            if elapsed_time >= time_to_asteroids:
                elapsed_time = 0
                # time_to_asteroids = max(time_to_asteroids - 900, 200)
                # number_of_row = min(number_of_row + 0.5, 10)

                # for _ in range(math.floor(number_of_row)):
                #     # self.asteroids.append(Asteroid(random.randint(0, self.width - 60), -60, 60, 60))
                #     self.asteroids.append(Asteroid(200, -60, 60, 60))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bullets.append(Bullet(self.player.x + self.player.width // 2 + 20, self.player.y - 6, 12, 50))
                        self.bullets.append(Bullet(self.player.x + self.player.width // 2 - 33, self.player.y - 6, 12, 50))

            for asteroid in self.asteroids:
                for hitBox in self.player.hitBoxes:
                    if ((asteroid.x < hitBox[0] < asteroid.x + asteroid.width) or (asteroid.x + asteroid.width > hitBox[0] + hitBox[2] > asteroid.x))\
                            and ((asteroid.y < hitBox[1] < asteroid.y + asteroid.height) or (hitBox[1] + hitBox[3] > asteroid.y and hitBox[1] < asteroid.y + asteroid.height)):

                        self.player.hit()

            self.draw()

        pygame.quit()


