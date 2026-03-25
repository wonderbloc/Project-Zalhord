import pygame
pygame.init()

from player import obj_player


class obj_game():
    def __init__(self):
        self.player = obj_player()