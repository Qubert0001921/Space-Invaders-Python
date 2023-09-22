from os import path
import pygame

ASSETS_PATH = "D:\\Kajtek\\Wszystko\\Programowanie\\Python\\SpaceInvadersActual\\assets"
ASSETS_IMG_PATH = path.join(ASSETS_PATH, "img")
ASSETS_FONT_PATH = path.join(ASSETS_PATH, "fonts")
ASSETS_SOUND_PATH = path.join(ASSETS_PATH, "sound")
FPS = 100
MAX_ASTEROID_VELOCITY = 600
GAME_NAME = "Space Invaders"
MUSIC_VOL = 0.5


def get_img_path(file_name):
    return path.join(ASSETS_IMG_PATH, file_name)


def get_sound_path(file_name):
    return path.join(ASSETS_SOUND_PATH, file_name)


def get_default_font(size):
    return pygame.font.Font(get_font_path("Silkscreen-Regular.ttf"), size)


def get_font_path(file_name):
    return path.join(ASSETS_FONT_PATH, file_name)