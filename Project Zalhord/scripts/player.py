import pygame
from math import cos
pygame.init()

from var import *

spr_perso = pygame.image.load("../sprites/player.png").convert_alpha()
spr_heart= pygame.image.load("../sprites/coeur.jpeg").convert_alpha()

class obj_heart(pygame.sprite.Sprite):
    def __init__(self): #Les variable du perso
        super().__init__ #Permet de relier un sprite plus tard
        self.size = 64
        self.margin = 32
        self.angle = 0
        self.image = spr_heart
        self.pos = [0,0]
        
    def draw_heart(self,surface,value):
        
            self.angle=(self.angle+0.05)%6.82

            for i in range(value):
                heart_sprite=jiggle(pygame.transform.scale(self.image,(self.size,self.size)),(screen_size[0]-(i+1)*(self.size+self.margin),self.margin),self.size,self.angle,-5) ##Mouvement balancier du joueur
                surface.blit(heart_sprite[0],heart_sprite[1])

class obj_player(pygame.sprite.Sprite): #Création du perso
    def __init__(self): #Les variable du perso
        super().__init__() #Permet de relier un sprite plus tard
        self.health = 3 #PV du perso
        self.mov=[0,0]  #Vélocité du perso [x,y]
        self.pos=(0,0)
        self.invicible_time=0
        self.angle=0
        self.amplitude = 15
        self.size= 80 #Taille du perso
        self.image= spr_perso #relie le sprite
        self.rect = pygame.Rect((0, 0), (32, 32))
        
        self.rect.x = 100
        self.rect.y=100
        self.heart= obj_heart()

    def draw_player(self,surface):
        self.amplitude= max(self.amplitude-(2),0)
        self.angle=(self.angle+0.075)%6.82
        player_sprite=jiggle(pygame.transform.scale(self.image,(self.size + self.amplitude,self.size+self.amplitude)),self.rect,self.size,self.angle,15) ##Mouvement balancier du joueur
        self.invicible_time = max(0,self.invicible_time-1)
        if cos(self.invicible_time) < 0:
            player_sprite[0].set_alpha(255-self.invicible_time*3)
            surface.blit(player_sprite[0], player_sprite[1]) #Affiche le joueur

        else:
            player_sprite[0].set_alpha(255)
            surface.blit(player_sprite[0], player_sprite[1]) #Affiche le joueur
    
    
