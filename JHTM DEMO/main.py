import pygame
from pygame.locals import *

pygame.init()

################################################################################
## Chargement des sprite
spr_background = pygame.image.load("sprites/background.jpg") 
spr_perso = pygame.image.load("sprites/tete.png")
spr_icone = pygame.image.load("sprites/crane.png")
##Création des Classe
class obj_player(pygame.sprite.Sprite): #Création du perso
    def __init__(self): #Les variable du perso
        super().__init__ #Permet de relier un sprite plus tard
        self.health = 3 #PV du perso
        self.mov=[0,0]  #Vélocité du perso [x,y]
        self.pos=[0.0]
        self.size=100 #Taille du perso
        self.image= spr_perso #relie le sprite
        self.rect =self.image.get_rect() #Choppe le rectangle de l'image (pour les collision)

class obj_game():
    def __init__(self):
        self.player = obj_player()

####Variables
#Fenetre
screen_size = (1920-50,1080-50) #Taille de la fenetre (-50 parce qu'on veut quand meme appuyer sur quitter)
screen = pygame.display.set_mode(screen_size)
fps = 24
#Tiles
gap=30
margin=30
tile_size= 100+margin
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

#Création des instance

game= obj_game()

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
    screen.blit(pygame.transform.scale_by(spr_perso,(game.player.size/spr_perso.size[0],game.player.size/spr_perso.size[1])),game.player.rect)

    # Re-collage des élémentsù


    # Rafraichissement
    pygame.display.flip()
    # Attente pour relancer la boucle
    pygame.time.Clock().tick(fps)
################################################################################
pygame.quit()