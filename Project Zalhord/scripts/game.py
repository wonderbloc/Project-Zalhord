import pygame
pygame.init()
from levels import *
from player import obj_player
from grid import *


class obj_game():
    def __init__(self,level):
        self.level = level.map
        self.player = obj_player()
        self.player.pos = level.start
        self.map = obj_tilemap(self.level)
        self.background = pygame.transform.scale(level.background,screen_size).convert()
        self.blured_background = pygame.transform.gaussian_blur(self.background,30)
