import pygame

###Consigne, chaque level doit etre un carrée, 0== un mur et 1== un chemin, si votre niveau n'est pas un carrée remplisser just le vide de mur


class level_2(): #Création du perso
    def __init__(self):
        self.map=[
            [0,1,1,1,0],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [0,1,1,1,0]
        ]
        self.start= (2,2)

        self.background = pygame.image.load("../sprites/kinger.gif") 

        self.ennemies = []

class level_1(): #Création du perso
    def __init__(self):
        self.map=[

            [2,2,2],
            [2,2,2],
            [2,2,2]

        ]
        self.start= (0,0)
        self.background = pygame.image.load("../sprites/level1234.png") 