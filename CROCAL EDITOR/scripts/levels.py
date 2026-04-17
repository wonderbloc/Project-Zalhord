import pygame
pygame.init()
TIME = "time"
ID = "id"
POS = "pos"
X="x"
Y="y"
TILE= "tile"
ROW="row"
COL="collumn"
MOV="mov"
BREAK = "break"
FLIP= "flip"

###Consigne, chaque level doit etre un carrée, 0== un mur et 1== un chemin, si votre niveau n'est pas un carrée remplisser just le vide de mur

class level_1(): #Création du perso
    def __init__(self):
        self.map=[

            [2,2,2],
            [2,2,2],
            [2,2,2]

        ]
        self.start= (0,0)
        self.rythme = 24
        self.background = pygame.image.load("../sprites/level1234.png") 
        self.ennemies = []
        self.music = "../musics/hopes_and_dream.mp3"

class level_2(): #Création du perso
    def __init__(self):
        self.map=[
            [0,1,0,1,0],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [0,1,1,1,0],
            [0,0,1,0,0]
        ]
        self.start= (2,1)
        self.music = "../musics/megalovania.mp3"
        self.background = pygame.image.load("../sprites/fond écran png.png").convert_alpha() 
        self.ennemies =  self.ennemies = [
             {TIME: 2,ID: "bounce",TILE:[1,1],MOV:[5,-30]},

        ]

class level_3(): #Création du perso
    def __init__(self):
        self.map=[
            [0,1,1,1,0],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [0,1,1,1,0]
        ]
        self.start= (2,2)

        self.background = pygame.image.load("../sprites/younggirl.jpg") 
        self.music = "../musics/young_girl.mp3"
        r=2.17
        self.ennemies = [
             {TIME: 4*r,ID: "rusher",POS:[540,540],MOV:[30,-5]},
             {TIME: 5*r,ID: "return",X:50,COL:2,MOV:[50,0]}, {TIME: 5*r,ID: "return",POS:[0,1080],MOV:[10,-40],BREAK:120},
             {TIME: 6*r,ID: "lober",POS:[1600,500],MOV:[-50,-60]},
             {TIME: 7*r,ID: "mirror",POS:[1600,0],FLIP:(False,True)},
             {TIME: 8*r,ID: "mirror",POS:[500,1000],FLIP:(False,True)},
             {TIME: 9*r,ID: "blind",POS:[500,1000]},

        ]