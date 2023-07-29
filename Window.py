import pygame
import game_config
from SpaceShip import SpaceShip
from Bullet import Bullet
from Asteroid import Asteroid
from scenes.SceneManager import SceneManager
from scenes.GameScene import GameScene
from scenes.TitleScene import TitleScene


class Window(object):
    def __init__(self, width, height, caption):
        pygame.init()
        pygame.font.init()

        self.width = width
        self.height = height
        self.caption = caption
        self.display = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        self.scene_manager = SceneManager([
            GameScene(self, self.clock),
            TitleScene(self, self.clock)
        ], 0)

        pygame.display.set_caption(self.caption)

    def draw(self):
        self.scene_manager.scenes[self.scene_manager.currentSceneIndex].draw()
        pygame.display.update()

    def mainloop(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                self.scene_manager.get_current_scene().handle_events(event)

            self.scene_manager.scenes[self.scene_manager.currentSceneIndex].mainloop()
            self.draw()
            self.scene_manager.check_to_change_scene()

        pygame.quit()


