#####Les importation
import pygame
from math import cos
from pygame.locals import *
from levels import *
from grid import*
from var import *
from game import obj_game
pygame.init()

################################################################################
#importer game

game=obj_game(screen_size,level_1,level_1_start) ##Load une instance du jeu

#Fonctions
def pressed(key):   ####renvoie une touche préssée
    return event.key in key

def reload_map():
    game.map=obj_game(screen_size,game.level,game.player.pos).map
    game.map.angle = map_angle

map_angle=0


# Ouverture de la fenêtre Pygame et collage du fond


# Rafraîchissement de l'écran
pygame.display.set_caption("JHTM") #Nom du projet
pygame.display.set_icon(pygame.transform.scale(game.player.image,(64,64))) #Icone du projet

################################################################################
# Boucle infinie ...
run = True
while run:
    #limits= 
    for event in pygame.event.get():    # Attente des événements
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == 27:
                game.map.level[0][2]=1
                reload_map()

             #Mouvement
            game.player.mov[0],game.player.mov[1]=(pressed(key_right)-pressed(key_left)),(pressed(key_down)-pressed(key_up)) #mouvement x et mouvement Y

            next_tile=game.map.select_tile((game.player.pos[0]+game.player.mov[0],game.player.pos[1]+game.player.mov[1])) ##Case séléctionner par le joueur

            if game.player.pos[0]+game.player.mov[0] >= 0 and game.player.pos[1]+game.player.mov[1] >= 0 and game.player.pos[1]+game.player.mov[1] < len(game.map.map_table) and game.player.pos[0]+game.player.mov[0] < len(game.map.map_table[-1]) and next_tile.id != "wall":
                game.player.pos=[game.player.pos[0]+game.player.mov[0],game.player.pos[1]+game.player.mov[1]] #applique les mouvement
                game.player.amplitude = 25
                
                

                    

        if event.type == VIDEORESIZE:
            screen_size=screen.get_size()
            reload_map()
            
            
 
            
  
    # Instructions
    # ...............

    screen.blit(pygame.transform.scale(spr_background,screen_size))
    

    game.map.draw_map(screen) ##dessine la map sur l'ecran
    game.player.rect = [game.map.select_tile(game.player.pos).rect.x  + (game.map.select_tile(game.player.pos).size-game.player.size)//2,game.map.select_tile(game.player.pos).rect.y  + (game.map.select_tile(game.player.pos).size-game.player.size)//2] ###set les coordonné du perso au coordonné de la tiles choisi + centre le joueur
    player_sprite=jiggle(pygame.transform.scale(game.player.image,(game.player.size+game.player.amplitude,game.player.size+game.player.amplitude)),game.player.rect,game.player.size,game.player.angle,15) ##Mouvement balancier du joueur
    screen.blit(player_sprite[0], player_sprite[1]) #Affiche le joueur
    game.player.angle=(game.player.angle+0.075+game.player.amplitude)%6.28
    game.player.amplitude= max(game.player.amplitude-8,0)
    map_angle =(map_angle+0.05)%6.28
    game.map.angle= map_angle


    # Re-collage des éléments



    # Rafraichissement
    pygame.display.flip()
    # Attente pour relancer la boucle)
    pygame.time.Clock().tick(fps)
################################################################################
pygame.quit()
