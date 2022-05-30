import pygame
from settings import jump_cooldown
import time


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16
        self.last_time_jumped = None

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.last_time_jumped is None or time.time() - self.last_time_jumped > jump_cooldown:
                self.jump()
                self.last_time_jumped = time.time()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        # self.apply_gravity()
