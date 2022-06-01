import pygame
import sys
from settings import *
from level import Level

# Setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(basic_level, screen)
level1 = Level(level_1, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            level1.moving_button = True
        elif event.type == pygame.MOUSEBUTTONUP:
            level1.moving_button = False

    screen.fill('black')
    level.run()
    pygame.display.update()
    clock.tick(60)
