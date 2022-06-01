import pygame
import sys
from settings import *
from level import Level
from support import draw_background

# Setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(basic_level, screen)
level1 = Level(level_1, screen)
vertical_offset = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            level1.moving_button = True
        elif event.type == pygame.MOUSEBUTTONUP:
            level1.moving_button = False

    draw_background(screen, vertical_offset)
    if vertical_offset < 64:
        vertical_offset += background_scroll_speed
    else:
        vertical_offset = 0

    level.run()
    pygame.display.update()
    clock.tick(60)
