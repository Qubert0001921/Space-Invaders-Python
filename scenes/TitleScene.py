import pygame
from scenes.BaseScene import BaseScene
import game_config
import colors
from FontRenderer import FontRenderer
from Position import Position
from CollideBox import CollideBox


class TitleScene(BaseScene):
    def __init__(self, window, clock):
        super().__init__("Title", "TITLE", window, clock)

        self.title_font = game_config.get_default_font(85)
        self.options_font = game_config.get_default_font(30)

        self.mouse_buttons = (0, 0, 0)
        self.mouse_collide_box = CollideBox(0, 0, 1, 1)

        self.play_option = self.options_font.render("Play", 0, colors.WHITE)
        self.settings_option = self.options_font.render("Settings", 0, colors.WHITE)

        self.play_option_collide_box = CollideBox(0, 0, self.play_option.get_width(), self.play_option.get_height())
        self.settings_option_collide_box = CollideBox(0, 0, self.settings_option.get_width(), self.settings_option.get_height())

    def draw(self):
        bg = pygame.image.load(game_config.get_img_path("title_screen_bg.jpg"))
        bg = pygame.transform.scale(bg, (self.window.display.get_width(), self.window.display.get_height()))
        self.window.display.blit(bg, (0, 0))

        title_text = self.title_font.render(game_config.GAME_NAME, 0, colors.WHITE)
        title_text_pos = Position(self.window.display.get_width()//2-title_text.get_width()//2, 110)

        self.window.display.blit(title_text, title_text_pos.to_tuple())

        font_renderer = FontRenderer(title_text_pos.x, title_text_pos.y + title_text.get_height() + 20, self.window.display, horizontal=False)

        self.play_option_collide_box.set_position(font_renderer.render(self.play_option, title_text.get_width() // 2 - self.play_option.get_width() // 2, 0))
        self.settings_option_collide_box.set_position(font_renderer.render(self.settings_option, title_text.get_width() // 2 - self.settings_option.get_width() // 2, 0))

        # pygame.draw.rect(self.window.display, colors.RED, self.play_option_collide_box.get_rect(), 2)
        # pygame.draw.rect(self.window.display, colors.RED, self.settings_option_collide_box.get_rect(), 2)

        super().draw()

    def handle_events(self, event):
        super().handle_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.on_play_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_buttons = pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONUP:
            if self.mouse_buttons[0]:
                mouse_pos = pygame.mouse.get_pos()
                self.mouse_collide_box.x = mouse_pos[0]
                self.mouse_collide_box.y = mouse_pos[1]

                if self.mouse_collide_box.check_if_collide([self.play_option_collide_box]):
                    self.on_play_pressed()

                if self.mouse_collide_box.check_if_collide([self.settings_option_collide_box]):
                    self.on_settings_pressed()

    def on_play_pressed(self):
        self.scene_to_change = "Game"

    def on_settings_pressed(self):
        self.scene_to_change = "Settings"

    def mainloop(self, deltatime):
        super().mainloop(deltatime)


