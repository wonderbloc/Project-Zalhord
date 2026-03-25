import pygame
from pygame.locals import *

pygame.init()

################################################################################
# Chargement des sprite

spr_background = pygame.image.load("sprites/background.jpg") 
spr_perso = pygame.image.load("sprites/tete.png")
spr_icone = pygame.image.load("sprites/crane.png")
####Variables
#Fenetre
screen_size = (1920-50,1080-50) #Taille de la fenetre (-50 parce qu'on veut quand meme appuyer sur quitter)
screen = pygame.display.set_mode(screen_size)
fps = 24
#Perso
perso_coo=[500,500] #coordonnée du perso
perso_mov=[0,0] #Vélocité du perso
perso_size=100 #Taille du perso
#Tiles
margin=5
tile_size= perso_size+margin
tile_number=3 #nombre de tile dans une ligne du carée
####Définition des touche
key_down=[115,1073741905] # S + Bas 
key_up=[122,1073741906] # Z + Haut
key_right=[100,1073741903] # D + droite
key_left=[113,1073741904] # Q+gauche
key_pause=[27] #echap
keys=[key_right,key_left,key_up,key_left] #liste des clé
#Fonctions
def pressed(key):
    return event.key in key
# Ouverture de la fenêtre Pygame et collage du fond

    # Attente pour relancer la boucle
    pygame.time.Clock().tick(fps)