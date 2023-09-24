import pygame

import colors
from scenes.BaseScene import BaseScene
import game_config
from SpaceShip import SpaceShip
from Asteroid import Asteroid
from Bullet import Bullet
from ObjectRenderer import ObjectRenderer
from CollideBox import CollideBox
import math
import random


class GameScene(BaseScene):
    def __init__(self, window, clock):
        super().__init__("Game", "CAPTION", window, clock)
        self.bg_img = pygame.image.load(game_config.get_img_path("space.png"))
        self.bg_img = pygame.transform.scale(self.bg_img, (self.window.width, self.window.height))

        self.player = SpaceShip(80, 100, self.window.display.get_width()//2 - 40, self.window.height - 110)
        self.bullets = []
        self.asteroids = []

        self.time_to_asteroids = 2000
        self.elapsed_time = 0
        self.number_of_row = 1

        self.game_over = True

        self.font_title = pygame.font.Font(game_config.get_font_path("Silkscreen-Regular.ttf"), 110)
        self.font_normal = pygame.font.Font(game_config.get_font_path("Silkscreen-Regular.ttf"), 25)

        self.score_hit = 0
        self.score_missed = 0

        self.weapon_heat = 0
        self.weapon_heat_max = 6

        self.time_to_cool_max = 2800
        self.time_to_cool = self.time_to_cool_max
        self.time_to_cool_elapsed = 0
        self.time_to_cool_min = 700

        self.time_to_start = 0000

        pygame.mixer.set_num_channels(10)

        self.engine_start_sound = pygame.mixer.Sound(game_config.get_sound_path("ship_start.wav"))

        self.asteroid_hit_sound = pygame.mixer.Sound(game_config.get_sound_path("ship_asteroid_hit.wav"))

        self.engine_running_sound = pygame.mixer.Sound(game_config.get_sound_path("ship_running_cont.wav"))

        self.warning_sound = pygame.mixer.Sound(game_config.get_sound_path("warning.wav"))

        self.overheat_sound = pygame.mixer.Sound(game_config.get_sound_path("notification.wav"))
        self.overheat_sound_played = False
        self.overheat_warning_border = (self.weapon_heat_max - 1 )/ self.weapon_heat_max

        self.explosion_sound = pygame.mixer.Sound(game_config.get_sound_path("explosion.wav"))

        self.shot_sound = pygame.mixer.Sound(game_config.get_sound_path("ship_shot.wav"))

        self.trigger_sound = pygame.mixer.Sound(game_config.get_sound_path("trigger.wav"))

        self.damage_text_color = colors.WHITE
        self.heat_text_color = colors.WHITE

        self.return_btn_text = self.font_normal.render("Return", 0, colors.EMPHASISE)
        self.return_btn_collideBox = CollideBox(0, 0, self.return_btn_text.get_width(), self.return_btn_text.get_height())
        self.mouse_collideBox = CollideBox(0, 0, 5, 5)
        self.mouse_btns = pygame.mouse.get_pressed()
        
    def init(self):
        super().init()
        print("NOW")
        self.engine_start_sound.set_volume(game_config.MUSIC_VOL)
        self.asteroid_hit_sound.set_volume(game_config.MUSIC_VOL)
        self.engine_running_sound.set_volume(game_config.MUSIC_VOL)
        self.warning_sound.set_volume(game_config.MUSIC_VOL)
        self.overheat_sound.set_volume(game_config.MUSIC_VOL * 2)
        self.explosion_sound.set_volume(game_config.MUSIC_VOL * 2)
        self.shot_sound.set_volume(game_config.MUSIC_VOL / 2)
        self.trigger_sound.set_volume(game_config.MUSIC_VOL * 10)

    def draw(self):
        super().draw()

        self.window.display.blit(self.bg_img, (0, 0))
        self.player.draw(self.window.display)

        score_hit_text = self.font_normal.render(f"HIT: {self.score_hit}", 0, (255, 255, 255))
        score_missed_text = self.font_normal.render(f"MISSED: {self.score_missed}", 0, (255, 255, 255))
        score_immunity_text = self.font_normal.render(f"DAMAGE: {round((self.player.immunity_max - self.player.immunity) / self.player.immunity_max * 100) }%", 0, self.damage_text_color)
        weapon_heat_text = self.font_normal.render(f"HEAT: {round(self.weapon_heat / self.weapon_heat_max * 100)}%", 0, self.heat_text_color)

        if not self.game_over:
            if self.time_to_start > 0:
                count_text_value = math.floor(self.time_to_start // 1000)
                count_text_content = str(count_text_value) if count_text_value > 0 else "START!"
                count_text = self.font_title.render(count_text_content, 0, colors.WHITE)
                self.window.display.blit(count_text, (self.window.display.get_width() // 2 - count_text.get_width()//2, self.window.display.get_height()//2 - count_text.get_height()))

            font_renderer = ObjectRenderer(15, 15, self.window.display, horizontal=False)
            text_y_margin = 0

            font_renderer.render(score_hit_text, 0, text_y_margin)
            font_renderer.render(score_missed_text, 0, text_y_margin)
            font_renderer.render(score_immunity_text, 0, text_y_margin)
            font_renderer.render(weapon_heat_text, 0, text_y_margin)

            for asteroid in self.asteroids:
                if asteroid.y > self.window.display.get_height():
                    self.asteroids.remove(asteroid)
                    self.score_missed += 1
                    continue

                asteroid.draw(self.window.display)
                asteroid.y += round(asteroid.velocity * self.deltatime)

            if self.time_to_start <= 0:
                self.player_movement()

                for bullet in self.bullets:
                    if bullet.y + bullet.height < 0 or bullet.y >= self.window.height:
                        self.bullets.remove(bullet)
                        continue

                    bullet.draw(self.window.display)
                    bullet.y -= round(bullet.velocity * self.deltatime)

        else:
            game_over_text = self.font_title.render("GAME OVER", 0, (255, 255, 255))
            game_over_text_pos = (self.window.display.get_width()//2 - game_over_text.get_width()//2, self.window.display.get_height()//2 - game_over_text.get_height()//2 - 100)

            self.window.display.blit(game_over_text, game_over_text_pos)

            font_renderer = ObjectRenderer(game_over_text_pos[0], game_over_text_pos[1] + game_over_text.get_height() + 2, self.window.display)
            between_text_margin = 30
            x_margin = (game_over_text.get_width() - score_hit_text.get_width() - score_missed_text.get_width() - between_text_margin) / 2

            font_renderer.render(score_hit_text, x_margin, 0)
            font_renderer.render(score_missed_text, between_text_margin, 0)

            return_btn_fr = ObjectRenderer(game_over_text_pos[0], game_over_text_pos[1] + game_over_text.get_height() + 4 + score_hit_text.get_height(), self.window.display, horizontal=False)
            self.return_btn_collideBox.set_position(return_btn_fr.render(self.return_btn_text,game_over_text.get_width() //2 - self.return_btn_text.get_width()//2,0))


            # pygame.draw.rect(self.window.display, colors.RED, (pos.x, pos.y, self.return_btn_text.get_width(), self.return_btn_text.get_height()), 2)
            # pygame.draw.rect(self.window.display, colors.RED, (pos_1.x, pos_1.y, score_hit_text.get_width(), score_hit_text.get_height()), 2)
            # pygame.draw.rect(self.window.display, colors.RED, (pos_2.x, pos_2.y, score_missed_text.get_width(), score_missed_text.get_height()), 2)

    def player_movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.x -= round(self.player.velocity * self.deltatime)
        elif keys[pygame.K_RIGHT]:
            self.player.x += round(self.player.velocity * self.deltatime)

    def on_defeat(self):
        self.game_over = True
        self.engine_running_sound.stop()
        self.engine_start_sound.stop()
        self.play_sound_once(self.explosion_sound)

    def handle_events(self, event):
        super().handle_events(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.time_to_start <= 0:
                self.play_sound_once(self.trigger_sound)
                shot = False

                if self.weapon_heat < self.weapon_heat_max:
                    if self.player.immunity < self.player.immunity_max:
                        if random.randrange(0, self.player.immunity_max - round(self.player.immunity) + 1) == 1:
                            self.bullets.append(Bullet(self.player.x + self.player.width // 2 + 20, self.player.y - 6))
                            self.weapon_heat += 0.5
                            shot = True
                        if random.randrange(0, self.player.immunity_max - round(self.player.immunity) + 1) == 1:
                            self.bullets.append(Bullet(self.player.x + self.player.width // 2 - 33, self.player.y - 6))
                            self.weapon_heat += 0.5
                            shot = True

                    else:
                        self.bullets.append(Bullet(self.player.x + self.player.width // 2 + 20, self.player.y - 6))
                        self.bullets.append(Bullet(self.player.x + self.player.width // 2 - 33, self.player.y - 6))
                        self.weapon_heat += 1
                        shot = True

                    if shot:
                        self.shot_sound.play()

                    if self.weapon_heat == self.weapon_heat_max and not self.overheat_sound_played:
                        self.play_sound_once(self.overheat_sound)
                        self.overheat_sound_played = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_btns = pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONUP:
            if self.mouse_btns[0]:

                mouse_pos = pygame.mouse.get_pos()
                self.mouse_collideBox.x = mouse_pos[0]
                self.mouse_collideBox.y = mouse_pos[1]

                if self.mouse_collideBox.check_if_collide([self.return_btn_collideBox]):
                    self.on_return_clicked()

    def play_sound_once(self, sound):
        if sound.get_num_channels() <= 0:
            sound.play(0)
    def on_return_clicked(self):
        self.scene_to_change = "Title"

    def mainloop(self, deltatime):
        super().mainloop(deltatime)
        # print(self.weapon_heat)

        if not self.game_over:

            self.deltatime = deltatime
            deltatime_ms = self.deltatime * 1000

            if 900 < self.time_to_start <= 1000:
                self.play_sound_once(self.engine_start_sound)

            if self.time_to_start <= 0:
                if self.engine_start_sound.get_num_channels() == 0:
                    self.play_sound_once(self.engine_running_sound)

                if self.weapon_heat / self.weapon_heat_max >= self.overheat_warning_border and self.weapon_heat != self.weapon_heat_max:
                    self.heat_text_color = colors.WARNING
                elif self.weapon_heat == self.weapon_heat_max:
                    self.heat_text_color = colors.HIGH_WARNING
                else:
                    self.heat_text_color = colors.WHITE

                self.elapsed_time += deltatime_ms
                self.time_to_cool_elapsed += deltatime_ms
                if self.elapsed_time >= self.time_to_asteroids:
                    self.elapsed_time = 0
                    self.time_to_asteroids = max(self.time_to_asteroids - 20, 150)
                    # self.number_of_row = min(self.number_of_row + 0.5, 10)
                    self.number_of_row = 1

                    for _ in range(math.floor(self.number_of_row)):
                        self.asteroids.append(Asteroid(random.randint(0, self.window.width - 60), -60, 60, 60))
                        # self.asteroids.append(Asteroid(200, -60, 60, 60))

                if self.time_to_cool_elapsed >= self.time_to_cool and self.weapon_heat > 0:
                    self.time_to_cool_elapsed = 0

                    if self.weapon_heat - 1 < 0:
                        self.weapon_heat = 0
                    else:
                        self.weapon_heat -= 1
                        if self.weapon_heat < self.weapon_heat_max:
                            self.overheat_sound_played = False

                    # self.time_to_cool = max(self.time_to_cool - (self.weapon_heat // 2 * 100), 200)
                    self.time_to_cool = max(self.weapon_heat / self.weapon_heat_max * self.time_to_cool_max, self.time_to_cool_min)
                    print((self.time_to_cool_max * max(self.weapon_heat_max - self.weapon_heat, 1) * 0.1))

                for asteroid in self.asteroids:
                    if asteroid.check_collision(self.player):
                        self.player.decrement_immunity(asteroid.velocity)
                        if self.player.immunity <= 0:
                            self.on_defeat()
                        self.asteroids.remove(asteroid)
                        self.play_sound_once(self.asteroid_hit_sound)

                        if self.player.immunity / self.player.immunity_max <= 0.18 and self.player.immunity > 0:
                            self.play_sound_once(self.warning_sound)
                            self.damage_text_color = colors.HIGH_WARNING
                        elif self.player.immunity / self.player.immunity_max <= 0.45 and self.player.immunity > 0:
                            self.damage_text_color = colors.WARNING
                        continue

                    if asteroid in self.asteroids:
                        for bullet in self.bullets:
                            if bullet.check_collision(asteroid):
                                self.asteroids.remove(asteroid)
                                self.bullets.remove(bullet)
                                self.score_hit += 1
            else:
                self.time_to_start -= deltatime_ms


