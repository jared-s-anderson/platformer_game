import pygame, sys

from displaySettings import *
from gameLevel import gameLevel
from gameData import level01
from playerClass import Player

pygame.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platforming Game')
level = gameLevel(level01, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('blue')
    level.run()
    pygame.display.update()

