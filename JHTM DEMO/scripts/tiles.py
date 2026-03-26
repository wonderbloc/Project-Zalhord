import pygame

spr_tiles = pygame.image.load("sprites/1_tiles.png")

class obj_player(pygame.sprite.Sprite): #Création du perso
    def __init__(self): #Les variable du perso
        super().__init__ #Permet de relier un sprite plus tard
        self.size= 64 #Taille du perso
        self.image= spr_tiles #relie le sprite
        self.rect =self.image.get_rect() #Choppe le rectangle de l'image (pour les collision