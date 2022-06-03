from os import walk
from settings import *
import pygame.image


def import_folder(path):
    surface_list = []

    for _,_,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image

            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)

    return surface_list


def draw_background(screen, vertical_offset):
    vertical_offset = int(vertical_offset)
    img_path = background_image
    img = pygame.image.load(img_path)
    screen.fill('black')

    width = 64
    height = 64
    for x in range(int(screen_width / width) + 1):
        for y in range(int(screen_height / height)):
            screen.blit(img, (x * width, y * height + vertical_offset - 64))


