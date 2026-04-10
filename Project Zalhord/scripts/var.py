import pygame
pygame.init()

from math import *
## Chargement des sprite
spr_background_MainMenu= pygame.image.load("../sprites/planet.jpg")
spr_icone = pygame.image.load("../sprites/logo.png")
spr_LogoJeu = pygame.image.load("../sprites/title.png")
spr_PublicitéMensongère = pygame.image.load("../sprites/image_publicitaire.png")
spr_MenuPause = pygame.image.load("../sprites/menu_pause.png")
spr_vide = pygame.image.load("../sprites/vide.png")
spr_Pause = pygame.image.load("../sprites/light-background.jpg")
spr_Altego = pygame.image.load("../sprites/altego.png")
spr_level1 = pygame.image.load("../sprites/level1234.png")
spr_level2 = pygame.image.load("../sprites/level2.png")
spr_background_final_boss = pygame.image.load("../sprites/fond écran png.png")

game_name="Project Zahlord"



####Variables
#Fenetre
mult=1
screen_size = (1920,1080) #Taille de la fenetre (-50 parce qu'on veut quand meme appuyer sur quitter)
screen = pygame.Surface(screen_size)
window_size= (screen_size[0]*mult,screen_size[1]*mult)
window= pygame.display.set_mode(window_size)
pygame.display.set_caption(game_name) #Nom du projet
pygame.display.set_icon(spr_icone) #Icone du projet
fps = 24
is_paused = False


#Tiles
next_tile=[]
####Définition des touche
key_down=[115,1073741905] # S + Bas 
key_up=[122,1073741906] # Z + Haut
key_right=[100,1073741903] # D + droite
key_left=[113,1073741904] # Q+gauche
key_pause=[27] #echap
key_plus= [1073741911,61]
key_minus=[1073741910,54]
keys_list=[key_right,key_left,key_up,key_down] #liste des clé
zoom_keys=[1073741911,61,1073741910,54]
keys=[]
for i in keys_list:
    for j in i:
        keys.append(j)




def jiggle(image,pos,size,angle,mult):
    rotate_sprite= pygame.transform.rotate(image,-cos(angle)*mult)
    center = rotate_sprite.get_rect(center=(pos[0]+size//2,pos[1]+size//2))
    return rotate_sprite, center


def distance(x1,y1,x2,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def vector(x1,y1,x2,y2):
    return [x2-x1,y2-y1]

def vector_normal(x1,y1,x2,y2,strenght):
    norm = distance(x1,y1,x2,y2)
    return [(x2-x1//norm)*strenght,(y2-y1//norm)*strenght]
