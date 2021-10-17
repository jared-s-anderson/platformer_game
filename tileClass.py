import pygame
from csvLayout import import_frames

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, shift):
        self.rect.x += shift

class FixedTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface

class Crate(FixedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load('graphics/crate.png').convert_alpha())
        offset = y + size
        self.rect = self.image.get_rect(bottomleft = (x, offset))

class Animation(Tile):
    def __init__(self, size, x, y, pathWay):
        super().__init__(size, x, y)
        self.frames = import_frames(pathWay)
        self.index = 0
        self.image = self.frames[self.index]

    def animate(self):
        self.index += .012
        if self.index >= len(self.frames):
            self.index = 0
        self.image = self.frames[int(self.index)]

    def update(self, shift):
        self.animate()
        self.rect.x += shift

class Coins(Animation):
    def __init__(self, size, x, y, pathWay):
        super().__init__(size, x, y, pathWay)
        x_center = x  + int(size / 2)
        y_center = y + int(size / 2)
        self.rect = self.image.get_rect(center = (x_center, y_center))
       