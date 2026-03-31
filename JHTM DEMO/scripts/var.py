import pygame
from math import cos
pygame.init()

## Chargement des sprite
spr_background = pygame.image.load("../sprites/kinger.gif") 
spr_icone = pygame.image.load("../sprites/crane.png")

        

def jiggle(image,pos,size,angle,mult):
    rotate_sprite= pygame.transform.rotate(image,-cos(angle)*mult)
    center = rotate_sprite.get_rect(center=(pos[0]+size//2,pos[1]+size//2))
    return rotate_sprite, center

####Variables
#Fenetre
screen_size = (1920//1.5,1080//1.5) #Taille de la fenetre (-50 parce qu'on veut quand meme appuyer sur quitter)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
fps = 24
#Tiles
next_tile=[]
####Définition des touche
key_down=[115,1073741905] # S + Bas 
key_up=[122,1073741906] # Z + Haut
key_right=[100,1073741903] # D + droite
key_left=[113,1073741904] # Q+gauche
key_pause=[27] #echap
keys=[key_right,key_left,key_up,key_left] #liste des clé