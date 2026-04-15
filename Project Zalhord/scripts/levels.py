import pygame
pygame.init()
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
        self.background = pygame.image.load("../sprites/fond écran png.png") 
        self.rythme = 24
        self.ennemies =  self.ennemies = [
             {"time": 4,"id": "stay","tiles":[540,540],"mov":[30,-5]},
             {"time": 0.5,"id": "return","pos":[50,540],"mov":[50,0]},
             {"time": 1.1,"id": "return","pos":[0,1080],"mov":[10,-40],"break":120},
             {"time": 5,"id": "lober","pos":[1600,500],"mov":[-50,-60]},
             {"time": 2,"id": "mirror","pos":[1600,0],"flip":(False,True)},
             {"time": 3,"id": "blind","pos":[1600,0]},

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
        self.ennemies = [
             {"time": 4,"id": "rusher","pos":[540,540],"mov":[30,-5]},
             {"time": 0.5,"id": "return","pos":[50,540],"mov":[50,0]},
             {"time": 1.1,"id": "return","pos":[0,1080],"mov":[10,-40],"break":120},
             {"time": 5,"id": "lober","pos":[1600,500],"mov":[-50,-60]},
             {"time": 2,"id": "mirror","pos":[1600,0],"flip":(False,True)},
             {"time": 3,"id": "blind","pos":[1600,0]},

        ]