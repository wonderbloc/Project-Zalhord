import pygame
pygame.init()
from levels import *
from player import obj_player
from grid import *


class obj_game():
    def __init__(self,size,init_pos):
        self.screen_size=size
        self.player = obj_player(init_pos)
        self.map = obj_tilemap(level_1,level_1_start,self.screen_size)