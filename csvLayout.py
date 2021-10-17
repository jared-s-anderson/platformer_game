import pygame
from csv import reader
from displaySettings import tile_size
from os import walk

def import_csv_layout(pathWay):
    terrainMap = []
    with open(pathWay) as map:
        levels = reader(map, delimiter = ',')
        for row in levels:
            terrainMap.append(list(row))
        return terrainMap

def import_graphics(pathWay):
    surface = pygame.image.load(pathWay).convert_alpha()
    tile_x = int(surface.get_size()[0] / tile_size)
    tile_y = int(surface.get_size()[1] / tile_size)

    tiles = []
    for row in range(tile_y):
        for col in range(tile_x):
            x = col * tile_size
            y = row * tile_size
            newSurface = pygame.Surface((tile_size, tile_size))
            newSurface.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            tiles.append(newSurface)
    return tiles

def import_frames(pathWay):
    img_surface_list = []
    for _,_, images in walk(pathWay):
        for i in images:
            dir = pathWay + '/' + i
            img_surface = pygame.image.load(dir).convert_alpha()
            img_surface_list.append(img_surface)
    return img_surface_list