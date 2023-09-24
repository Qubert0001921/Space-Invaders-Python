import pygame
import game_config
from SpaceShip import SpaceShip
from Bullet import Bullet
from Asteroid import Asteroid
from scenes.SceneManager import SceneManager
from scenes.GameScene import GameScene
from scenes.TitleScene import TitleScene
from scenes.SettingsScene import SettingsScene
import time


class Window(object):
    def __init__(self, width, height, caption):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        pygame.mouse.set_visible(False)

        self.width = width
        self.height = height
        self.caption = caption
        self.display = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        self.scene_manager = SceneManager([
            TitleScene(self, self.clock),
            GameScene(self, self.clock),
            SettingsScene(self, self.clock)
        ], 2)

        self.cursor_images = [pygame.image.load(game_config.get_img_path("arrow_cursor1.png")), pygame.image.load(game_config.get_img_path("hand_cursor2.png"))]
        self.cursor_images = [pygame.transform.scale(x, (x.get_width()//2, x.get_height()//2) ) for x in self.cursor_images]
        self.current_cursor = 0

        pygame.display.set_caption(self.caption)

    def draw(self):
        self.scene_manager.scenes[self.scene_manager.currentSceneIndex].draw()
        self.display.blit(self.cursor_images[self.current_cursor], pygame.mouse.get_pos())

        pygame.display.update()

    def mainloop(self):
        run = True

        previous_time = time.time()
        while run:
            tick = self.clock.tick(game_config.FPS)

            dt = time.time() - previous_time
            previous_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                self.scene_manager.get_current_scene().handle_events(event)


            self.scene_manager.scenes[self.scene_manager.currentSceneIndex].mainloop(dt)
            self.draw()
            self.scene_manager.check_to_change_scene()


        pygame.quit()


