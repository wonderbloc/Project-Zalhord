"""
Note:
Tutoriel pour creer une barre de chargement : https://www.youtube.com/watch?v=_D-_OmR36Pk
Tutoriel pour le joueur et comprendre les Class: https://www.youtube.com/watch?v=8J8wWxbAdFg&list=PLMS9Cy4Enq5KsM7GJ4LHnlBQKTQBV8kaR
Tutoriel utiliser comme base pour les tiles :https://www.youtube.com/watch?v=37phHwLtaFg
Formule pour avoir l'angle du vecteur : https://miniwebtool.com/fr/calculateur-angle-entre-vecteurs/
Calculer le produit scalaire python sans l'angle: https://www.delftstack.com/fr/howto/python/python-dot-product/
Sprite original de la guitar :https://www.megavoxels.com/learn/how-to-make-a-pixel-art-guitar/
Chat GPT a été utilisé pour comprendre certain message d'erreur ou pour comprendre sous quel angle résoudre certain probleme , Chat GPT n'a ni était utilisé pour généré du code ni était utilisé pour généré d'image.

"""

import pygame
from pygame.locals import *
from buttons import *
from var import *
from game import obj_game
from levels import *
from grid import *
from random import *
pygame.init()
pygame.mixer.init()

################################################################################

music = False

launch_images = ("../sprites/kinger.gif","../sprites/kinger_hacker.png")


spr_launch = pygame.image.load(launch_images[randint(0,len(launch_images)-1)]).convert()
spr_launch_size = spr_launch.get_rect().size
spr_launch = pygame.transform.scale(spr_launch,(480,int(spr_launch_size[1]/spr_launch_size[0]*480)))
pygame.display.quit()
screen_launching= pygame.display.set_mode((480,int(spr_launch_size[1]/spr_launch_size[0]*480)))

launching = True
pygame.display.set_caption("Loading..") #Nom du projet
pygame.display.set_icon(spr_icone)



screen_launching.blit(spr_launch,(0,0))
pygame.display.flip() #Charge tout


game_list = [obj_game(level_1()),obj_game(level_2()),obj_game(level_3())]





pygame.display.quit()


window= pygame.display.set_mode(window_size)


#Fonctions
def pressed(key):
    return event.key in key


map_angle=0




def change_state(state,level): 
    
    global etat
    global game
    etat = state
    if type(level) == int:
       pygame.mixer.music.stop()
       game = game_list[level]
       game.reset_game()
       pygame.mixer.music.load(game.music)
       pygame.mixer.music.play()
       

       

def toggle_pause():
    global is_paused
    
    is_paused = not(is_paused)
    if is_paused == True:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
def quit_game():
    global run
    run = False
    



# Ouverture de la fenêtre Pygame et collage du fond

#importer game






# Rafraîchissement de l'écran
pygame.display.set_caption(game_name) #Nom du projet
pygame.display.set_icon(spr_icone) #Icone du projet

################################################################################

music = False
def draw_buttons(surface,mult):
    for button in buttons:
        button.draw_button(surface,mult)
# Boucle infinie ...
debug = False


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
                
            if pressed([49]):
                debug = not(debug)
                if debug:
                    fps = 1
                else: 
                    fps =24
            if etat == "level":
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
        music=False
        if is_paused == False:
            
            screen.blit(pygame.transform.scale(game.background,screen_size))
            buttons=[obj_button(spr_b_pause,(25,25),(64,64), toggle_pause)]
            game.map.draw_map(screen) ##dessine la map sur l'ecran
            game.player.draw_player(screen)
            game.player.rect.x, game.player.rect.y = game.map.select_tile(game.player.pos).rect.x  + (game.map.select_tile(game.player.pos).size-game.player.size)//2,game.map.select_tile(game.player.pos).rect.y  + (game.map.select_tile(game.player.pos).size-game.player.size)//2 ###set les coordonné du perso au coordonné de la tiles choisi + centre le joueur
            game.create_ennemies(screen)
        else:
            
            screen.blit(pygame.transform.scale(game.blured_background,screen_size))
            buttons=[obj_button(spr_b_continue,(screen_size[0]//2-300,100),(600,130), toggle_pause),
                     obj_button(spr_b_continue,(screen_size[0]//2-300,300),(600,130), lambda : change_state("menu","nan nan uh uh"))
                     ]
    else:
        is_paused = False
        flip[0] = False
        flip[1] = False
        obs[0]=0
        if music == False:
            pygame.mixer.music.load("../musics/hip_shop.mp3")
            pygame.mixer.music.play(-1)
            music = True
        if etat == "menu":
            buttons= [obj_button(spr_b_jouer,(75,400),(480,130), lambda: change_state("menu_level", "none")),
                      obj_button(spr_b_jouer,(75,800),(480,130), quit_game )]
            screen.blit(pygame.transform.scale(spr_background_MainMenu,screen_size),(0,0))

            screen.blit(pygame.transform.scale(spr_LogoJeu,(600,400)),(screen_size[0]-880,screen_size[1]-490))
        
        elif etat =="menu_level":
            screen.blit(pygame.transform.scale(spr_background_MainMenu,screen_size),(0,0))
            buttons= [obj_button(spr_b_level_1,(50,50),(480,270), lambda: change_state("level",0)),
                    obj_button(spr_b_level_2,(50,370),(480,270), lambda: change_state("level",1)),
                    obj_button(spr_b_level_3,(50,370+320),(480,270), lambda: change_state("level",2))]
    
    screen=pygame.transform.flip(screen,flip[0],flip[1])
    filtre = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    filtre.fill((0, 0, 0, obs[0]))
    screen.blit(filtre)
    obs[0]=max(0,obs[0]-obs[1])

    draw_buttons(screen,mult)
    if etat == "level":
        game.player.heart.draw_heart(screen,game.player.health)
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