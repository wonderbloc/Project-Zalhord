import pygame
pygame.init()
from var import *
from levels import *
from player import obj_player
from grid import *
from ennemies import *
from copy import deepcopy



class obj_game():
    def __init__(self,level):
        self.level = level
        self.player = obj_player()
        self.player.pos = self.level.start
        self.map = obj_tilemap(self.level.map)
        self.background = pygame.transform.scale(self.level.background,screen_size).convert_alpha()
        self.blured_background = pygame.transform.gaussian_blur(self.background,10)
        self.ennemies_list = []
        self.ennemies_list = deepcopy(self.level.ennemies)
        self.timer = 0
        self.ennemies =[]
        self.music = self.level.music

    def reset_game(self):
        self.player.pos = self.level.start
        self.player.health = 3
        self.player.invicible_time = 0
        self.ennemies_list = []
        self.ennemies_list = deepcopy(self.level.ennemies)
        self.ennemies =[]
        self.timer = 0

    def create_ennemies(self,surface):
        for i in range(len(self.ennemies_list)):
            if type(self.ennemies_list[i]) == dict:
                if self.ennemies_list[i].get("time")*fps - wait <= self.timer:
                    self.ennemies.append(obj_ennemy())
                    for cle in self.ennemies_list[i].keys():
                        if cle == "id":
                            self.ennemies[-1].id = self.ennemies_list[i][cle]
                        if cle == "pos":
                            self.ennemies[-1].rect.topleft = self.ennemies_list[i][cle]
                        if cle == "x":
                            self.ennemies[-1].rect.x = self.ennemies_list[i][cle]
                        if cle == "y":
                            self.ennemies[-1].rect.y = self.ennemies_list[i][cle]
                        if cle == "tile":
                            self.ennemies[-1].rect.x, self.ennemies[-1].rect.y = self.map.select_tile(self.ennemies_list[i][cle]).rect.x  + ((self.map.select_tile(self.ennemies_list[i][cle])).size-64)//2, self.map.select_tile(self.ennemies_list[i][cle]).rect.y  + ((self.map.select_tile(self.ennemies_list[i][cle])).size-64)//2
                        if cle == "row":
                            self.ennemies[-1].rect.x = self.map.select_tile([self.ennemies_list[i][cle],0]).rect.x  + ((self.map.select_tile([self.ennemies_list[i][cle],0])).size-64)//2
                        if cle == "collumn":
                            self.ennemies[-1].rect.y = self.map.select_tile([0,self.ennemies_list[i][cle]]).rect.y  + (((self.map.select_tile([0,self.ennemies_list[i][cle]]))).size-64)//2
                        if cle == "mov":
                            self.ennemies[-1].mov = self.ennemies_list[i][cle]
                        if cle == "break":
                            self.ennemies[-1].break_time = self.ennemies_list[i][cle]
                        if cle == "flip":
                            self.ennemies[-1].flip = self.ennemies_list[i][cle]
                        
                    self.ennemies_list[i]=0

        self.ennemies_list = [i for i in self.ennemies_list if i != 0]

        self.timer += 1

        for i in range(len(self.ennemies)):
            if self.ennemies[i] !=0:
                if self.ennemies[i].actif:
                    self.ennemies[i].draw_ennemy(surface)
                    if pygame.Rect.colliderect(self.ennemies[i].rect,self.player.rect) and self.player.invicible_time <= 0 and self.ennemies[i].waiting == False and self.ennemies[i].damage == True :
                        self.player.health  -= 1
                        self.player.invicible_time = 36
                else:
                    self.ennemies[i] = 0
        

        self.ennemies = [i for i in self.ennemies if i != 0]
