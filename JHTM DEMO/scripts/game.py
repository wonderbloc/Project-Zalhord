import pygame
pygame.init()
from levels import *
from player import obj_player
from grid import *


class obj_game():
    def __init__(self,size,level,init_pos):
        self.level =level
        self.start=level_1_start
        self.screen_size=size
        self.player = obj_player(init_pos)
        self.map = obj_tilemap(self.level,self.start,self.screen_size)