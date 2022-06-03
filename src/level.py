"""
Represents one level the player can play. Stores information about the player,
tiles on the screen, and GUI information. Takes in level information from
settings.py to create the level
"""
import enum
from settings import *
from tiles import *
from player import Player
from support import import_folder


class Level:
    def __init__(self, level_data, surface):

        self.player = None
        self.tiles = None
        self.goal_tile = None
        self.moveable_buttons = None
        # Basic level setup
        self.display_surface = surface
        self.level_data = level_data

        self.world_shift = 0
        self.level_won = False

        # Dealing with moving the buttons
        self.moving_button = False
        self.mouse_pos = None
        self.prev_clicked_button = None
        self.left_button = None
        self.space_button = None
        self.right_button = None
        self.graphics = {}
        self.init_buttons()

        self.init_level(level_data)

    def init_level(self, layout):
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

    def restart_level(self):
        self.init_buttons()
        self.init_level(self.level_data)

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

        for sprite in self.moveable_buttons.sprites():
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
                        self.level_won = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        for sprite in self.moveable_buttons.sprites():
            if sprite.rect.colliderect(player.rect):
                # If our player collides with any tile in the level, check its direction first
                if player.direction.y > 0:
                    # Standing on top of a tile
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def import_character_assets(self):
        character_path = '../res/main/Menu/'  # ../res/character/
        self.graphics = {'gui': []}

        for animation in self.graphics.keys():
            full_path = character_path + animation
            self.graphics[animation] = import_folder(full_path)

    def init_buttons(self):
        """
        Initializes the moveable buttons to their correct spots in the dashboard
        """
        self.moveable_buttons = pygame.sprite.Group()
        self.import_character_assets()
        # Constants to change button layout
        left_right_center_offset = 150
        distance_from_screen_height = 84
        square_size = 64
        space_button_width = 64

        # Left Button
        # Set the default value, change it if specified in the arguments
        left_pos = (screen_width / 2 - left_right_center_offset,
                    screen_height - distance_from_screen_height)
        self.left_button = MoveableButton(left_pos, square_size, square_size)
        self.left_button.image = self.graphics['gui'][0]
        self.left_button.image = pygame.transform.scale(self.left_button.image, (64, 64))

        # Space Button
        space_pos = (screen_width / 2, screen_height - distance_from_screen_height)
        self.space_button = MoveableButton(space_pos, space_button_width, square_size)
        self.space_button.image = self.graphics['gui'][1]
        self.space_button.image = pygame.transform.scale(self.space_button.image, (64, 64))

        # Right Button
        right_pos = (screen_width / 2 + left_right_center_offset, screen_height - distance_from_screen_height)
        self.right_button = MoveableButton(right_pos, square_size, square_size)
        self.right_button.image = self.graphics['gui'][2]
        self.right_button.image = pygame.transform.scale(self.right_button.image, (64, 64))

        self.moveable_buttons.add(self.left_button)
        self.moveable_buttons.add(self.space_button)
        self.moveable_buttons.add(self.right_button)

    def manage_gui(self, mouse_pos=None, button=None):
        """
        Draws the gui at the bottom of the screen, displaying things like right left and space,
        and stats on how many deaths/time stuff like that
        """
        # Get the size of the screen and draw a rectangle at the bottom
        pygame.draw.rect(self.display_surface, (0, 255, 255),
                         pygame.Rect(0, screen_height - gui_height, screen_width, screen_height))

        # Draws the background of the gui
        img_path = gui_image
        img = pygame.image.load(img_path)
        width = 64
        height = 64
        for x in range(int(screen_width / width) + 1):
            for y in range(int(gui_height / height) + 1):
                self.display_surface.blit(img, (x * width, y * height + screen_height - gui_height))

        # TODO: Make this so that the buttons can be replaced and the player can then take that action
        if button == ButtonType.Left:
            self.player.sprite.can_move_left = False
            self.moveable_buttons.sprites()[0].update_pos(mouse_pos)
        elif button == ButtonType.Space:
            self.player.sprite.can_jump = False
            self.moveable_buttons.sprites()[1].update_pos(mouse_pos)
        elif button == ButtonType.Right:
            self.player.sprite.can_move_right = False
            self.moveable_buttons.sprites()[2].update_pos(mouse_pos)

    def draw_gui_moveable_buttons(self):
        button_list = [ButtonType.Left, ButtonType.Space, ButtonType.Right]
        if not self.moving_button:
            self.manage_gui()
            self.prev_clicked_button = None
            return
        # If we are moving a button, check to see if a button has been clicked and if so update its position to
        # the mouse position
        self.mouse_pos = pygame.mouse.get_pos()
        for i, sprite in enumerate(self.moveable_buttons.sprites()):
            if sprite.rect.collidepoint(self.mouse_pos):
                self.manage_gui(self.mouse_pos, button_list[i])
                self.prev_clicked_button = button_list[i]
                sprite.placed = True
                return
            else:
                self.manage_gui(self.mouse_pos, self.prev_clicked_button)

    def draw_gui_moveable_buttons_old(self):
        button_list = [ButtonType.Left, ButtonType.Space, ButtonType.Right]
        if self.moving_button:
            self.mouse_pos = pygame.mouse.get_pos()
        if self.mouse_pos:
            for i, sprite in enumerate(self.moveable_buttons.sprites()):
                if sprite.rect.collidepoint(self.mouse_pos):
                    self.manage_gui(self.mouse_pos, button_list[i])
                    self.mouse_pos = None
                    self.prev_clicked_button = button_list[i]
                    sprite.placed = True
                    return
            self.manage_gui()
        else:
            self.manage_gui()

    def check_player_won_died_restart(self):
        if self.level_won:
            # Will change later, for now just restart the level
            self.level_won = False
            self.restart_level()

        if self.player.sprite.rect.centery > 615:
            self.restart_level()

        if self.player.sprite.restart_level:
            self.restart_level()

    def run(self):
        # Level Tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        # GUI Stuff
        self.draw_gui_moveable_buttons()
        self.moveable_buttons.update(self.world_shift)
        self.moveable_buttons.draw(self.display_surface)

        # PLayer Group
        self.player.update()  # Updates to check if the player should move
        self.horizontal_movement_collision()  # Check for horizontal collisions
        self.vertical_movement_collision()  # Check for vertical collisions
        self.player.draw(self.display_surface)  # Draw the player

        # Checking if a player has died or won the level
        self.check_player_won_died_restart()
        self.scroll_x()


class ButtonType(enum.Enum):
    Left = 1
    Space = 2
    Right = 3
