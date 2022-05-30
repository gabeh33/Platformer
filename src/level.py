import pygame
from settings import *
from tiles import *
from player import Player


class Level():
    def __init__(self, level_data, surface):

        self.player = None
        self.tiles = None
        self.goal_tile = None
        self.moveable_buttons = None
        # Basic level setup
        self.display_surface = surface
        self.level_data = level_data
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        """
        Draws the tiles that make up the level according to the given layout
        :param layout: Array of strings that describe the layout of the level
        """
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()


        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif cell == 'P':
                    player = Player((x, y))
                    self.player.add(player)
                elif cell == 'G':
                    goal = Tile((x, y), tile_size, True)
                    self.tiles.add(goal)


    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 5

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # If our player collides with any tile in the level, check its direction first
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # If our player collides with any tile in the level, check its direction first
                if player.direction.y > 0:
                    # Standing on top of a tile
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    if sprite.isGoal:
                        print("LEVEL COMPLETED")
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def manage_gui(self):
        """
        Draws the gui at the bottom of the screen, displaying things like right left and space,
        and stats on how many deaths/time stuff like that
        """
        # Get the size of the screen and draw a rectangle at the bottom
        pygame.draw.rect(self.display_surface, (0, 255, 255),
                         pygame.Rect(0, screen_height - gui_height, screen_width, screen_height))

        self.moveable_buttons = pygame.sprite.Group()

        # Constants to change button layout
        left_right_center_offset = 150
        distance_from_screen_height = 84
        square_size = 64
        space_button_width = 128

        # Left Button
        left_button = MoveableButton((screen_width / 2 - left_right_center_offset,
                                      screen_height - distance_from_screen_height), square_size, square_size)
        self.moveable_buttons.add(left_button)

        # Space Button
        space_button = MoveableButton((screen_width / 2, screen_height - distance_from_screen_height),
                                      space_button_width, square_size)
        self.moveable_buttons.add(space_button)

        # Right Button
        right_button = MoveableButton((screen_width / 2 + left_right_center_offset,
                                       screen_height - distance_from_screen_height), square_size, square_size)
        self.moveable_buttons.add(right_button)

        self.moveable_buttons.draw(self.display_surface)

    def check_player_died(self):
        # print(self.player.sprite.rect.centery)
        if self.player.sprite.rect.centery > 700:
            self.setup_level(self.level_data)

    def run(self):
        # Level Tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # PLayer Group
        self.player.update()  # Updates to check if the player should move
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        # GUI Stuff
        self.manage_gui()

        # Checking if a player has died
        self.check_player_died()


