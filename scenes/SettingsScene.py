from scenes.BaseScene import BaseScene
import game_config
import pygame

class SettingsScene(BaseScene):
    def __init__(self, window, clock):
        super().__init__("Settings", "Settings", window, clock)
        self.bg = pygame.image.load(game_config.get_img_path("settings_bg.png"))
        self.bg = pygame.transform.scale(self.bg, (window.display.get_width(), window.display.get_height()))
        
    def draw(self):
        self.window.display.blit(self.bg, (0, 0))

        super().draw()
    
    def mainloop(self, deltatime):
        super().mainloop(deltatime)
