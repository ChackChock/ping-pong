from random import randint
import pygame
from scripts.sprite import Sprite


class Ball(Sprite):
    def __init__(self, center, image, speed):
        super().__init__(center, image)

        self.velocity = pygame.Vector2()
        self.center = pygame.Vector2(center)
        self.speed = speed

    def reset(self, display_center):
        self.center.update(display_center)

        if randint(0, 1):
            self.velocity.update(self.speed, 0)
        else:
            self.velocity.update(- self.speed, 0)

    def bounce(self, rocket):
        mult = (self.rect.centery - rocket.rect.centery) / rocket.rect.height

        if self.velocity.x > 0:
            self.rect.right = rocket.rect.left
            self.velocity.rotate_ip(45 * mult)
        else:
            self.rect.left = rocket.rect.right
            self.velocity.rotate_ip(- 45 * mult)

        self.center.x = self.rect.centerx
        self.velocity.x *= - 1

    def update(self, display_height):
        self.center += self.velocity
        self.rect.center = self.center

        if self.rect.top < 0:
            self.rect.top = 0
            self.center.y = self.rect.centery
            self.velocity.y = - self.velocity.y

        if self.rect.bottom > display_height:
            self.rect.bottom = display_height
            self.center.y = self.rect.centery
            self.velocity.y = - self.velocity.y
