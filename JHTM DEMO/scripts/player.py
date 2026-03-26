import pygame
pygame.init()

from var import spr_perso


class obj_player(pygame.sprite.Sprite): #Création du perso
    def __init__(self): #Les variable du perso
        super().__init__ #Permet de relier un sprite plus tard
        self.health = 3 #PV du perso
        self.mov=[0,0]  #Vélocité du perso [x,y]
        self.pos=[0.0]
        self.size=100 #Taille du perso
        self.image= spr_perso #relie le sprite
        self.rect =self.image.get_rect() #Choppe le rectangle de l'image (pour les collision)