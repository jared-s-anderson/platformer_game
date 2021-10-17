import pygame
from tileClass import Animation

class Enemies(Animation):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, 'graphics/enemy_movement')
        self.rect.y += size - self.image.get_size()[1]
        self.velocity = 1

    def movement(self):
        self.rect.x += self.velocity

    def flip_image(self):
        if self.velocity > 0:
            self.image = pygame.image.transform.flip(self.image, True, False)

    def reverse(self):
        self.velocity *= -1

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.movement()