import pygame
from scenes.BaseScene import BaseScene
import game_config
import colors
from ObjectRenderer import ObjectRenderer
from Position import Position
from Label import Label
from CollideBox import CollideBox


class TitleScene(BaseScene):
    def __init__(self, window, clock):
        super().__init__("Title", "TITLE", window, clock)

        self.title_font = game_config.get_default_font(85)
        self.options_font = game_config.get_default_font(30)

        self.mouse_buttons = (0, 0, 0)
        self.mouse_collide_box = CollideBox(0, 0, 1, 1)

        # self.play_option = self.options_font.render("Play", 0, colors.WHITE)
        self.play_option = Label(Position(0, 0), self.options_font, "Play", colors.WHITE, hittable=True)

        # self.settings_option = self.options_font.render("Settings", 0, colors.WHITE)
        self.settings_option = Label(Position(0, 0), self.options_font, "Settings", colors.WHITE, hittable=True)

    def init(self):
        super().init()
        self.window.current_cursor = 0

    def draw(self):
        bg = pygame.image.load(game_config.get_img_path("title_screen_bg.jpg"))
        bg = pygame.transform.scale(bg, (self.window.display.get_width(), self.window.display.get_height()))
        self.window.display.blit(bg, (0, 0))

        title_text = self.title_font.render(game_config.GAME_NAME, 0, colors.WHITE)
        title_text_pos = Position(self.window.display.get_width()//2-title_text.get_width()//2, 110)

        self.window.display.blit(title_text, title_text_pos.to_tuple())

        font_renderer = ObjectRenderer(title_text_pos.x, title_text_pos.y + title_text.get_height() + 20, self.window.display, horizontal=False)

        font_renderer.render(self.play_option, title_text.get_width() // 2 - self.play_option.width // 2, 0)
        font_renderer.render(self.settings_option, title_text.get_width() // 2 - self.settings_option.width // 2, 0)

        # pygame.draw.rect(self.window.display, colors.RED, self.play_option.collide_boxes[0].get_rect(), 2)
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

                if self.mouse_collide_box.check_if_collide(self.play_option.collide_boxes):
                    self.on_play_pressed()

                if self.mouse_collide_box.check_if_collide(self.settings_option.collide_boxes):
                    self.on_settings_pressed()

    def on_play_pressed(self):
        self.scene_to_change = "Game"

    def on_settings_pressed(self):
        self.scene_to_change = "Settings"

    def update_mouse_collide_box(self):
        mouse_pos = pygame.mouse.get_pos()
        self.mouse_collide_box.x = mouse_pos[0]
        self.mouse_collide_box.y = mouse_pos[1]

    def mainloop(self, deltatime):
        super().mainloop(deltatime)
        self.update_mouse_collide_box()

        # TODO DO STH WITH THIS SHIT!

        if self.mouse_collide_box.check_if_collide(self.play_option.collide_boxes):
            self.settings_option.change_color(colors.WHITE)
            self.play_option.change_color(colors.EMPHASISE)
            self.window.current_cursor = 1
        elif self.mouse_collide_box.check_if_collide(self.settings_option.collide_boxes):
            self.settings_option.change_color(colors.EMPHASISE)
            self.play_option.change_color(colors.WHITE)
            self.window.current_cursor = 1
        else:
            self.settings_option.change_color(colors.WHITE)
            self.play_option.change_color(colors.WHITE)
            self.window.current_cursor = 0


