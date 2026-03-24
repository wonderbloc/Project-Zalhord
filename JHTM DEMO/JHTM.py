import pygame
from pygame.locals import *

pygame.init()

################################################################################
# Chargement du fond

spr_background = pygame.image.load("sprites/background.jpg")
spr_perso = pygame.image.load("sprites/tete.png")
spr_icone = pygame.image.load("sprites/crane.png")
#Variables
screen_size = (1920-50,1080-50)
fps = 24
tile_size=64
tile_number=3
perso_coo=[500,500]
perso_mov=[0,0]
#
key_down=[115,1073741905]
key_up=[122,1073741906]
key_right=[100,1073741903]
key_left=[113,1073741904]
key_pause=[27]
keys=[key_right,key_left,key_up,key_left]
#Fonctions
def pressed(key):
    return event.key in key
# Ouverture de la fenêtre Pygame et collage du fond

screen = pygame.display.set_mode(screen_size)

fond=spr_background.convert()


# Rafraîchissement de l'écran
pygame.display.set_caption("JHTM")
pygame.display.set_icon(spr_background)

## Constantes
    # Taux de rafraichissement (fps = frame per second)

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
            perso_mov[0],perso_mov[1]=(pressed(key_right)-pressed(key_left))*tile_size,(pressed(key_down)-pressed(key_up))*tile_size
            perso_coo[0],perso_coo[1]=perso_coo[0]+perso_mov[0],perso_coo[1]+perso_mov[1]
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