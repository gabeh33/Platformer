from level import Level
import pygame
from enum import Enum
from support import *
from tiles import *


class Menu:
    def __init__(self, screen):
        # Init
        self.screen = screen
        self.page = MenuPage.main
        self.graphics = None
        self.level_won = False

        # Background variables
        self.horizontal_offset = 0

        # Main menu buttons
        self.main_buttons = pygame.sprite.Group()
        self.top_button = None
        self.second_button = None
        self.third_button = None

        self.import_menu_assets()

    def import_menu_assets(self):
        character_path = '../res/main/Menu/'  # ../res/character/
        self.graphics = {'Buttons': []}

        for button in self.graphics.keys():
            full_path = character_path + button
            self.graphics[button] = import_folder(full_path)

    # ================================ Main Menu Methods ================================ #
    def draw_main_menu_buttons(self):
        top_pos = (center_x, top_button_to_top_screen)
        image_dimensions = (menu_button_width, menu_button_height)
        self.top_button = DefaultButton(top_pos, menu_button_width, menu_button_height)
        self.top_button.set_image(self.graphics['Buttons'][7], image_dimensions)

        self.second_button = DefaultButton((center_x, top_button_to_top_screen + button_spacing),
                                           menu_button_width, menu_button_height)
        self.second_button.set_image(self.graphics['Buttons'][0], image_dimensions)

        self.third_button = DefaultButton((center_x, top_button_to_top_screen + button_spacing * 2),
                                          menu_button_width, menu_button_height)
        self.third_button.set_image(self.graphics['Buttons'][4], image_dimensions)

        self.main_buttons.add(self.top_button)
        self.main_buttons.add(self.second_button)
        self.main_buttons.add(self.third_button)

        self.main_buttons.draw(self.screen)

    def run_main_menu_page(self):
        draw_background_horizontal(self.screen, self.horizontal_offset, yellow_background)
        self.horizontal_offset = self.horizontal_offset + background_scroll_speed if self.horizontal_offset < 64 else 0

        self.draw_main_menu_buttons()

    def main_menu_mbu(self):
        """
        Handles mouse button up for the main menu
        """
        for i, sprite in enumerate(self.main_buttons.sprites()):
            if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                pages = [MenuPage.play, MenuPage.levels, MenuPage.settings]
                self.page = pages[i]
                return

    # ================================ Level Selector Methods ================================ #
    def run_levels_page(self):
        print("Running level page")
        self.screen.fill('black')

    def levels_mbu(self):
        pass

    # ================================ Settings Methods ================================ #
    def run_settings_page(self):
        print("Running settings page")
        self.screen.fill('green')

    def settings_mbu(self):
        pass

    # ================================ Functionality Methods ================================ #
    def handle_mouse_button_down(self):
        pass

    def handle_mouse_button_up(self):
        for i, sprite in enumerate(self.main_buttons.sprites()):
            if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                sprite.image.fill('red')
                # pages = [MenuPage.play, MenuPage.levels, MenuPage.settings]
                # self.page = pages[i]
                return

    def run(self):
        if self.page == MenuPage.main:
            self.run_main_menu_page()
        elif self.page == MenuPage.levels:
            self.run_levels_page()
        elif self.page == MenuPage.settings:
            self.run_settings_page()


class MenuPage(Enum):
    main = 1  # Default shows all the options that the player can choose
    levels = 2  # Level shows all the different levels to choose from
    settings = 3  # Displays settings that the user can change, including picking a character
    play = 4  # Player clicked the play button

