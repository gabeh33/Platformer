import pygame
import sys
from settings import *
from level import Level
from menu import Menu

class Controller:
    def __init__(self, levels):
        self.levels = levels

    def run(self):
        # Setup
        pygame.init()
        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()

        curr_level = 0

        level_to_run = Level(self.levels[curr_level], screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    level_to_run.handle_mouse_button_down()
                elif event.type == pygame.MOUSEBUTTONUP:
                    level_to_run.handle_mouse_button_up()

            level_to_run.run()

            if level_to_run.level_won:
                curr_level += 1
                if curr_level >= len(self.levels):
                    curr_level = 0

                level_to_run = Level(self.levels[curr_level], screen)

            pygame.display.update()
            clock.tick(60)


class MenuController(Controller):
    def __init__(self):
        super().__init__(None)

    def run(self):
        # Setup
        pygame.init()
        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()

        curr_level = 0

        menu = Menu(screen)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    menu.handle_mouse_button_down()
                elif event.type == pygame.MOUSEBUTTONUP:
                    menu.handle_mouse_button_up()

            menu.run()

            pygame.display.update()
            clock.tick(60)
