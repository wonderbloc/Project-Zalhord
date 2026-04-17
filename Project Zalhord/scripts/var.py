import pygame
pygame.init()

from math import *
## Chargement des sprite
spr_background_MainMenu= pygame.image.load("../sprites/planet.jpg")
spr_icone = pygame.image.load("../sprites/logo.png")
spr_LogoJeu = pygame.image.load("../sprites/title.png")



game_name="Project Zalhord"



####Variables
#Fenetre
wait= 30
mult=1
screen_size = (1920,1080) #Taille de la fenetre (-50 parce qu'on veut quand meme appuyer sur quitter)
screen = pygame.Surface(screen_size)
window_size= (screen_size[0]*mult,screen_size[1]*mult)
obs=[0,1]
screen_launching= pygame.display.set_mode((480,1))
 #Icone du projet
fps = 24
is_paused = False
flip = [False,False]
etat = "menu"


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


def change_flip(table):
    global flip
    if table[0] == True:
        flip[0] = not(flip[0])
    if table[1] == True:
        flip[1] = not(flip[1])


def sign(n):
    if n !=0:
        return n/abs(n)
    else:
        return 0

def jiggle(image,pos,size,angle,mult):
    rotate_sprite= pygame.transform.rotate(image,cos(angle)*mult)
    if type(size) == int:
        center = rotate_sprite.get_rect(center=(pos[0]+size//2,pos[1]+size//2))
    else:
        center = rotate_sprite.get_rect(center=(pos[0]+size[0]//2,pos[1]+size[1]//2))
    return rotate_sprite, center

def rotate(image,pos,size,angle):
    rotate_sprite= pygame.transform.rotate(image,angle)
    if type(size) == int:
        center = rotate_sprite.get_rect(center=(pos[0]+size//2,pos[1]+size//2))
    else:
        center = rotate_sprite.get_rect(center=(pos[0]+size[0]//2,pos[1]+size[1]//2))
    return rotate_sprite, center

def distance(pos1,pos2):
    return ((pos2[0]-pos1[0])**2+(pos2[1]-pos1[1])**2)**0.5

def vector_norm(pos1,pos2,norm):
    return [norm*((pos2[0]-pos1[0])/distance(pos1,pos2)) , norm*((pos2[1]-pos1[1])/distance(pos1,pos2))]



def get_angle(vector):
    a=(0,1)
    b=vector
    b_norm = (b[0]**2+b[1]**2)**(0.5)
    return (acos(sum([i * j for (i, j) in zip(a, b)])/b_norm)* (180 / 3.141592))
