from os import path

ASSETS_PATH = "D:\\Kajtek\\Wszystko\\Programowanie\\Python\\SpaceInvadersActual\\assets"
ASSETS_IMG_PATH = path.join(ASSETS_PATH, "img")
FPS = 60

def get_img_path(file_name):
    return path.join(ASSETS_IMG_PATH, file_name)