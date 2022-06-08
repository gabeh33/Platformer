import pygame
from support import import_folder
from settings import tile_size


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, tile_type='grass', is_goal=False):
        super().__init__()
        self.graphics = {}
        self.import_character_assets()

        self.image = self.graphics[tile_type][0]

        # self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(topleft=pos)
        self.isGoal = is_goal

    def import_character_assets(self):
        character_path = '../res/main/Terrain/'  # /res/main/Main Characters/Virtual Guy/
        self.graphics = {'grass': [],
                         'goal': []}

        for img in self.graphics.keys():
            full_path = character_path + img
            self.graphics[img] = import_folder(full_path)

    def update(self, x_shift):
        """
        Shifts this given tile to the left or right
        :param x_shift: The direction and amount to shift the Tile
        """
        self.rect.x += x_shift


class MoveableButton(pygame.sprite.Sprite):
    def __init__(self, pos, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect(center=pos)
        self.placed = False

    def update(self, x_shift):
        if self.placed:
            self.rect.x += x_shift

    def update_pos(self, pos):
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    def set_image(self, image, size):
        self.image = image
        self.scale_image(size)

    def scale_image(self, new_size):
        self.image = pygame.transform.scale(self.image, new_size)


class DefaultButton(MoveableButton):
    def __init__(self, pos, width, height, image=None):
        super().__init__(pos, width, height)
        if image is not None:
            self.image = image
