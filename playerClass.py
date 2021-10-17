import pygame
import os

class Player():
   def __init__(self, standing, x, y, velocity):
       self.x = x
       self.y = y
       self.velocity = velocity
       self.standing = standing
       self.move_left = []
       self.move_right = []

       self.left = False
       self.right = False
       self.walk = 0

def movement(self, folder_name):
        fileList = os.listdir(f"graphics/{folder_name}")
        for file in fileList:
            if 'right' in file:
                self.move_right.append(pygame.image.load(f"graphics/{folder_name}/{file}"))
            elif 'left' in file:
                self.move_left.append(pygame.image.load(f"graphics/{folder_name}/{file}"))

def move(self, key):
    if key[pygame.K_LEFT]:
        self.x -= self.velocity
        self.left = True
        self.right = False

    elif key[pygame.K_RIGHT]:
        self.x += self.velocity
        self.left = False
        self.right = True
    
    else:
        self.walk = 0

def renderCharacter(self, win):
    if self.walk + 1 >= 12:
        self.walk = 0
    if self.right:
        win.blit(self.move_right[self.walk // 4], (self.x, self.y))
        self.walk += 1
    elif self.left:
        win.blit(self.move_left[self.walk // 4], (self.x, self.y))
        self.walk += 1
    else:
        win.blit(self.standing, (self.x, self.y))




