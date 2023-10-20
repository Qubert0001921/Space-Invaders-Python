import colors
from scenes.BaseScene import BaseScene
from ObjectRenderer import ObjectRenderer
from Position import Position
from Slider import Slider
from CollideBox import CollideBox
from Label import Label
import game_config
import pygame


class SettingsScene(BaseScene):
    def __init__(self, window, clock):
        super().__init__("Settings", "Settings", window, clock)
        self.bg = pygame.image.load(game_config.get_img_path("settings_bg.png"))
        self.bg = pygame.transform.scale(self.bg, (window.display.get_width(), window.display.get_height()))
        self.title_font = game_config.get_default_font(85)
        self.back_btn_font = game_config.get_default_font(70)
        self.options_font = game_config.get_default_font(28)

        self.mouse_collideBox = CollideBox(0, 0, 1, 1)
        self.mouse_btn_clicked = (0, 0, 0)

        self.music_volume_slider = Slider(game_config.MUSIC_VOL * 100, 100, 0, Position(0, 0), 300, 10, colors.WHITE, colors.LIGHT_GRAY)
        self.fps_slider = Slider(game_config.FPS, game_config.FPS_MAX, 1, Position(0, 0), 300, 10, colors.WHITE, colors.LIGHT_GRAY)

        self.music_volume_opt = Label((0, 0), self.options_font, "Music Volume", colors.WHITE)
        self.fps_opt = Label((0, 0), self.options_font, "FPS", colors.WHITE)

        self.back_btn = Label(Position(20, 30), self.back_btn_font, "<", colors.WHITE, hittable=True)

    def handle_events(self, event):
        super().handle_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.on_back_button_pressed()

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_btn_clicked = pygame.mouse.get_pressed()

        if event.type == pygame.MOUSEBUTTONUP:
            if self.mouse_btn_clicked[0]:
                if self.mouse_collideBox.check_if_collide(self.back_btn.collide_boxes):
                    self.on_back_button_pressed()

    def init(self):
        super().init()
        self.window.current_cursor = 0

    def on_back_button_pressed(self):
        self.save_settings()
        self.scene_to_change = "Title"

    def save_settings(self):
        game_config.MUSIC_VOL = self.music_volume_slider.value / 100
        game_config.FPS = self.fps_slider.value

    def draw(self):
        self.window.display.blit(self.bg, (0, 0))
        title_text = self.title_font.render(game_config.GAME_NAME, 0, colors.WHITE)

        general_menu = self.options_font.render("general", 0, colors.WHITE)

        # music_volume_opt = self.options_font.render("Music Volume", 0, colors.WHITE)
        # music_volume_opt = Text(self.options_font, "Music volume", colors.WHITE)
        # fps_opt = self.options_font.render("FPS", 0, colors.WHITE)
        # fps_opt = Text(self.options_font, "FPS", colors.WHITE)

        menu_margin_top = self.back_btn.text.get_height() + 40
        menu_margin_x = 20
        menu_margin_y = 20
        menu_width = self.window.display.get_width() - 2 * menu_margin_x
        menu_bg_width = 0.23 * menu_width
        menu_height = self.window.display.get_height() - menu_margin_top - menu_margin_y

        menu_bg = pygame.image.load(game_config.get_img_path("moreBlack.png")).convert_alpha()
        menu_bg = pygame.transform.scale(menu_bg, (menu_bg_width, menu_height))
        menu_bg.set_alpha(200)

        options_bg = pygame.image.load(game_config.get_img_path("moreBlack.png")).convert_alpha()
        options_bg = pygame.transform.scale(options_bg, (menu_width - menu_bg_width, menu_height))
        options_bg.set_alpha(160)

        self.window.display.blit(title_text, (self.window.display.get_width()//2 - title_text.get_width()//2, 20))
        self.back_btn.draw(self.window.display)

        self.window.display.blit(menu_bg, (menu_margin_x, menu_margin_top))

        options_bg_pos = Position(menu_margin_x + menu_bg.get_width(), menu_margin_top)
        self.window.display.blit(options_bg, options_bg_pos.to_tuple())

        self.window.display.blit(general_menu, (menu_margin_x + menu_bg.get_width()//2 - general_menu.get_width()//2, menu_bg.get_height()//2 - general_menu.get_height() + menu_margin_top))

        options_margin_x = 40
        options_margin_y = 70
        options_fr = ObjectRenderer(options_bg_pos.x + options_margin_x, options_bg_pos.y + options_margin_y, self.window.display, horizontal=False)

        options_fr.render(self.music_volume_opt, 0, 0)
        options_fr.render(self.fps_opt, 0, 0)

        music_volume_slider_value = self.options_font.render(f"{round(self.music_volume_slider.value / self.music_volume_slider.max_value * 100)}%", 0, colors.WHITE)
        self.music_volume_slider.pos_bar = Position(self.music_volume_opt.pos.x + self.music_volume_opt.width + 30, self.music_volume_opt.pos.y + self.music_volume_opt.height//2 - 5)
        self.music_volume_slider.change_value(self.music_volume_slider.value)
        self.music_volume_slider.draw(self.window.display)

        # pygame.draw.rect(self.window.display, colors.RED, self.music_volume_slider.collide_boxes[0].get_rect(), 2)

        self.window.display.blit(music_volume_slider_value, (self.music_volume_opt.pos.x + self.music_volume_opt.width + self.music_volume_slider.width + 60, self.music_volume_opt.pos.y))

        self.fps_slider.pos_bar = Position(self.music_volume_opt.pos.x + self.music_volume_opt.width + 30, self.fps_opt.pos.y + self.fps_opt.height//2 - 5)
        self.fps_slider.change_value(self.fps_slider.value)
        self.fps_slider.draw(self.window.display)

        self.window.display.blit(self.options_font.render(str(self.fps_slider.value), 0, colors.WHITE), (self.music_volume_opt.pos.x + self.music_volume_opt.width + self.fps_slider.width + 60, self.fps_opt.pos.y))

        # pygame.draw.rect(self.window.display, colors.RED, self.fps_slider.collide_boxes[0].get_rect(), 2)

        super().draw()

    def check_keyboard_input(self):
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            if self.mouse_collideBox.check_if_collide(self.music_volume_slider.collide_boxes):
                l = self.mouse_collideBox.x - self.music_volume_slider.pos_bar.x
                value = round(l * self.music_volume_slider.max_value / self.music_volume_slider.width)
                self.music_volume_slider.change_value(value)

            elif self.mouse_collideBox.check_if_collide(self.fps_slider.collide_boxes):
                l = self.mouse_collideBox.x - self.fps_slider.pos_bar.x
                value = round(l * self.fps_slider.max_value / self.fps_slider.width)
                self.fps_slider.change_value(value)

    def update_mouse_collide_box(self):
        mouse_pos = pygame.mouse.get_pos()
        self.mouse_collideBox.x = mouse_pos[0]
        self.mouse_collideBox.y = mouse_pos[1]

    def mainloop(self, deltatime):
        super().mainloop(deltatime)
        self.check_keyboard_input()
        self.update_mouse_collide_box()

        if self.mouse_collideBox.check_if_collide(self.back_btn.collide_boxes):
            self.back_btn.change_color(colors.EMPHASISE)
            self.window.current_cursor = 1
        else:
            self.back_btn.change_color(colors.WHITE)
            self.window.current_cursor = 0
