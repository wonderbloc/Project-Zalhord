import pygame
from pygame.locals import *

from buttons import *
from var import *
from game import obj_game
from levels import *
from grid import *
pygame.init()

################################################################################


game_list = (obj_game(level_1()),obj_game(level_2()))



#Fonctions
def pressed(key):
    return event.key in key


map_angle=0

global etat
global game

def change_state(state,level): 
   global etat
   global game
   etat = state
   if type(level) == int:
       game = game_list[level]

def toggle_pause():
    global is_paused
    is_paused = not(is_paused)

is_blured = False


# Ouverture de la fenêtre Pygame et collage du fond

#importer game



# Rafraîchissement de l'écran
pygame.display.set_caption("JHTM") #Nom du projet
pygame.display.set_icon(spr_icone) #Icone du projet


################################################################################
etat = "menu"
#buttons= [obj_button("play",(75,400), lambda: change_state("menu_level"))]
music = False
def draw_buttons(surface,mult):
    for button in buttons:
        button.draw_button(surface,mult)
# Boucle infinie ...
run = True
while run:
   
   
    for event in pygame.event.get():    # Attente des événements
        if event.type == QUIT:
            run = False
        if event.type == MOUSEBUTTONDOWN :
            for bouton in buttons:
                bouton.interact()
        if event.type == KEYDOWN :

            if pressed(zoom_keys) and int(max(0.25,min(mult + ((pressed(key_plus) - pressed(key_minus))/4),1,25))*4) != int(mult*4):
                mult= max(0.25,min(mult + ((pressed(key_plus) - pressed(key_minus))/4),1.25))
                
                pygame.display.quit()
                window_size = (int(screen_size[0]*mult),int(screen_size[1]*mult))
                pygame.display.set_caption(game_name) #Nom du projet
                pygame.display.set_icon(spr_icone) #Icone du projet
                window =pygame.display.set_mode(window_size)

            
        if event.type == KEYDOWN and etat == "menu":
            if event.key == 115:
                pygame.mixer.music.play()
                music = True
            if event.key == 27:
                if music:
                    pygame.mixer.music.pause()
                    music = False
                else :
                    pygame.mixer.music.unpause()
                    music = True
            if event.key == 13:
                pygame.mixer.music.stop()
                music = False
                
        if event.type == KEYDOWN and etat == "level":
            if is_paused == False:
                #Mouvement
                game.player.mov[0],game.player.mov[1]=(pressed(key_right)-pressed(key_left)),(pressed(key_down)-pressed(key_up)) #mouvement x et mouvement Y

                next_tile=game.map.select_tile((game.player.pos[0]+game.player.mov[0],game.player.pos[1]+game.player.mov[1])) ##Case séléctionner par le joueur

                if pressed(keys) and game.player.pos[0]+game.player.mov[0] >= 0 and game.player.pos[1]+game.player.mov[1] >= 0 and game.player.pos[1]+game.player.mov[1] < len(game.map.map_table) and game.player.pos[0]+game.player.mov[0] < len(game.map.map_table[-1]) and next_tile.id != "wall":
                    game.player.pos=[game.player.pos[0]+game.player.mov[0],game.player.pos[1]+game.player.mov[1]] #applique les mouvement
                    game.player.amplitude = 15
                    next_tile.amplitude = 30
            if event.key == 27 :
                toggle_pause()
                
                
    
        
         
    if etat == "level":
        
        if is_paused == False:
            screen.blit(pygame.transform.scale(game.background,screen_size))
            buttons=[obj_button(spr_b_pause,(25,25),(48,48), toggle_pause)]
            game.map.draw_map(screen) ##dessine la map sur l'ecran
            game.player.draw_player(screen)
            game.player.rect.x, game.player.rect.y = game.map.select_tile(game.player.pos).rect.x  + (game.map.select_tile(game.player.pos).size-game.player.size)//2,game.map.select_tile(game.player.pos).rect.y  + (game.map.select_tile(game.player.pos).size-game.player.size)//2 ###set les coordonné du perso au coordonné de la tiles choisi + centre le joueur
            game.player.heart.draw_heart(screen,game.player.health)
        else:
            screen.blit(pygame.transform.scale(game.blured_background,screen_size))
            buttons=[obj_button(spr_b_continue,(screen_size[0]//2-300,100),(600,130), toggle_pause),
                     obj_button(spr_b_continue,(screen_size[0]//2-300,300),(600,130), lambda : change_state("menu","nope"))
                     ]
    else:
        is_paused = False
        if etat == "menu":
            buttons= [obj_button(spr_b_jouer,(75,400),(480,130), lambda: change_state("menu_level", "none"))]
            screen.blit(pygame.transform.scale(spr_background_MainMenu,screen_size),(0,0))
            
            screen.blit(pygame.transform.scale(spr_LogoJeu,(600,400)),(screen_size[0]-880,screen_size[1]-490))
        
        elif etat =="menu_level":
            screen.blit(pygame.transform.scale(spr_background_MainMenu,screen_size),(0,0))
            buttons= [obj_button(pygame.transform.scale(spr_b_level_1,(330,190)),(770,360),(240*2,135*2), lambda: change_state("level",0)),
                    obj_button(pygame.transform.scale(spr_b_level_2,(345,190)),(330,550),(240*2,135*2), lambda: change_state("level",1))]
            
    
    

    if is_paused==True :
        screen=pygame.transform.grayscale(screen)
    draw_buttons(screen,mult)
    # Instructions
    # ...............
    window.blit(pygame.transform.scale(screen,window_size))
    # Re-collage des élémentsù

    # Rafraichissement
    pygame.display.flip()
    # Attente pour relancer la boucle
    pygame.time.Clock().tick(fps)
################################################################################
pygame.quit()