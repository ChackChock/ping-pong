import pygame


class Sprite:
    def __init__(self, center, image):
        self.image = image.copy()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=center)

    def collide_sprite(self, other):
        return pygame.sprite.collide_mask(self, other)

    def render(self, display):
        display.blit(self.image, self.rect)
