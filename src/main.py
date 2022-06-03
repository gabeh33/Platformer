#  A simple platformer game built by Gabe Holmes
#  This is the main event loop, run this file to run the game
#
import pygame
import sys
from settings import *
from level import Level
from support import draw_background

# Setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
vertical_offset = 0

# Levels
level = Level(basic_level, screen)
level1 = Level(level_1, screen)

level_to_run = level1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            level_to_run.moving_button = not level_to_run.moving_button
        # elif event.type == pygame.MOUSEBUTTONUP:
        # level_to_run.moving_button = False

    draw_background(screen, vertical_offset)
    vertical_offset = vertical_offset + background_scroll_speed if vertical_offset < 64 else 0

    level_to_run.run()
    pygame.display.update()
    clock.tick(60)
