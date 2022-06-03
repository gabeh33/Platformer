import pygame
from settings import *
import time
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Information relating to animating the character
        self.animations = {}
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        
        self.image = self.animations['idle'][self.frame_index]
        self.image = pygame.transform.scale(self.image, (54, 63))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)

        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16
        self.last_time_jumped = None

        self.can_move_right = True
        self.can_jump = True
        self.can_move_left = True

        self.restart_level = False

    def import_character_assets(self):
        """
        Imports the assets needed to animate the character and stores them in self.animations
        """
        character_path = character_info
        self.animations = {'idle': [],
                           'run': [],
                           'jump': [],
                           'fall': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        """
        Animates the player by cycling through image files
        """
        animation = self.animations['idle']
        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def get_input(self):
        """
        Gets the input from the player. Also checks if the player can move left, right, or jump
        based on if they are using the controller boxes to help them in the level
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.can_move_right:
                self.direction.x = 1
            else:
                self.direction.x = 0
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.can_move_left:
                self.direction.x = -1
            else:
                self.direction.x = 0
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            if (self.last_time_jumped is None or time.time() - self.last_time_jumped > jump_cooldown) and self.can_jump:
                self.jump()
                self.last_time_jumped = time.time()
        if keys[pygame.K_r]:
            self.restart_level = True

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.animate()
