import pygame
from pygame.locals import *

from grid import*
from var import *
from game import obj_game
pygame.init()

################################################################################
#Fonctions
def pressed(key):
    return event.key in key


# Ouverture de la fenêtre Pygame et collage du fond

#importer game
level=[
    [1,1,0],
    [1,1,1],
    [0,1,1]
]
game=obj_game()
map = obj_tilemap(level)
map_pos = [screen_size[0]//2-(map.map_w//2),screen_size[1]//2-(map.map_h//2)]
map.self_start_x,map.self_start_y=map_pos[0], map_pos[1]

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
            if event.key == 27:
                pass
             #Mouvement
            game.player.mov[0],game.player.mov[1]=(pressed(key_right)-pressed(key_left))*(tile_size+gap),(pressed(key_down)-pressed(key_up)) #mouvement x et mouvement Y
            game.player.pos=[game.player.pos[0]+game.player.mov[0],game.player.pos[1]+game.player.mov[1]] #applique les mouvement

            
  
    # Instructions
    # ...............
    
    screen.fill((0,0,255))
    map.start_x,map.start_y= map_pos[0], map_pos[1]
    map.draw_map(screen)
    game.player.rect = map.select_tile((0,1))
    screen.blit(pygame.transform.scale(game.player.image,(game.player.size,game.player.size)),game.player.rect)

    # Re-collage des éléments



    # Rafraichissement
    pygame.display.flip()
    # Attente pour relancer la boucle
    pygame.time.Clock().tick(fps)
################################################################################
pygame.quit()
