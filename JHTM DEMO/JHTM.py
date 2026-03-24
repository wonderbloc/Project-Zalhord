import pygame
from pygame.locals import *

pygame.init()

################################################################################
# Chargement des sprite

spr_background = pygame.image.load("sprites/background.jpg") 
spr_perso = pygame.image.load("sprites/tete.png")
spr_icone = pygame.image.load("sprites/crane.png")
####Variables
#Systeme
screen_size = (1920-50,1080-50) #Taille de la fenetre (-50 parce qu'on veut quand meme appuyer sur quitter)
fps = 24
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

screen = pygame.display.set_mode(screen_size)

fond=spr_background.convert()


# Rafraîchissement de l'écran
pygame.display.set_caption("JHTM") #Nom du projet
pygame.display.set_icon(spr_background) #Icone du projet

################################################################################
# Boucle infinie ...
run = True
while run:
   
    for event in pygame.event.get():    # Attente des événements
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            #Passer en booléan
           
            if event.key in keys and not(pressed(key_pause)):
                ##pygame.mixer.music.play()
                music = True
            if event.key == 27:
                if music:
                    print("yEAAAAH")
                   ## pygame.mixer.music.pause()
                    music = False
                else :
                    print("Oh Nooo")
                    ##pygame.mixer.music.unpause()
                    music = True
             #Mouvement
            perso_mov[0],perso_mov[1]=(pressed(key_right)-pressed(key_left))*tile_size,(pressed(key_down)-pressed(key_up))*tile_size #mouvement x et mouvement Y
            perso_coo[0],perso_coo[1]=perso_coo[0]+perso_mov[0],perso_coo[1]+perso_mov[1] #applique les mouvement
            print(pressed(key_right), event.key)
  
    # Instructions
    # ...............
    
    screen.fill((255,255,255))
    screen.blit(pygame.transform.scale_by(spr_perso,(tile_size/spr_perso.size[0],tile_size/spr_perso.size[1])),perso_coo)

    # Re-collage des élémentsù


    # Rafraichissement
    pygame.display.flip()
    # Attente pour relancer la boucle
    pygame.time.Clock().tick(fps)
################################################################################
pygame.quit()