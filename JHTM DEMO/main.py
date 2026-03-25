import pygame
from pygame.locals import *


from var import *
from classes.game import obj_game
pygame.init()

################################################################################

#Fonctions
def pressed(key):
    return event.key in key


# Ouverture de la fenêtre Pygame et collage du fond

#importer game

game=obj_game()

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
            game.player.mov[0],game.player.mov[1]=(pressed(key_right)-pressed(key_left))*(tile_size+gap),(pressed(key_down)-pressed(key_up))*(tile_size+gap) #mouvement x et mouvement Y
            game.player.rect.x,game.player.rect.y=game.player.rect.x+game.player.mov[0],game.player.rect.y+game.player.mov[1] #applique les mouvement
            print(pressed(key_right), event.key)
  
    # Instructions
    # ...............
    
    screen.fill((0,0,255))
    # Re-collage des élémentsù


    # Rafraichissement
    pygame.display.flip()
    # Attente pour relancer la boucle
    pygame.time.Clock().tick(fps)
################################################################################
pygame.quit()