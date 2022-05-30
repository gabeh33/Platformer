import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, is_goal=False):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey') if not is_goal else self.image.fill('green')
        self.rect = self.image.get_rect(topleft=pos)
        self.isGoal = is_goal

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

    def update(self, x_pos_center, y_pos_center):
        self.rect.centerx = x_pos_center
        self.rect.centery = y_pos_center
