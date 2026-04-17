import pygame
from var import *
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

center = (screen_size[0]//2,screen_size[1]//2)

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
        self.rythme = 24
        self.ennemies =  self.ennemies = [
             {TIME: 2,ID: "bounce",TILE:[1,1],MOV:[5,-30]},
             {TIME: 0,ID: "lober",COL:0, X:-150 ,MOV:[-60,-30]},
             {TIME: 0,ID: "lober",COL:0, X:150 ,MOV:[60,-30]},

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
        hz = 2.16667/4
        self.background = pygame.image.load("../sprites/younggirl.jpg") 
        self.music = "../musics/young_girl.mp3"
        self.ennemies = [
            #INTRO
            {TIME: 2*hz,ID: "rusher",COL: 0,X:50,MOV:[30,0]},
            {TIME: 3*hz,ID: "rusher",COL: 1,X:50,MOV:[30,0]},
            {TIME: 4*hz,ID: "rusher",COL: 2,X:50,MOV:[30,0]},
            {TIME: 5*hz,ID: "rusher",COL: 3,X:50,MOV:[30,0]},
            {TIME: 6*hz,ID: "rusher",COL: 4,X:50,MOV:[30,0]},
            {TIME: 7*hz,ID: "rusher",ROW: 0,Y:50,MOV:[0,50]},{TIME: 7*hz,ID: "rusher",ROW: 4,Y:50,MOV:[0,500]},
            {TIME: 8*hz,ID: "rusher",ROW: 1,Y:-50,MOV:[0,-50]},{TIME: 8*hz,ID: "rusher",ROW: 3,Y:-50,MOV:[0,-50]},
            {TIME: 9*hz,ID: "rusher",ROW: 2,Y:50,MOV:[0,50]},
            {TIME: 10*hz,ID: "mirror",POS:[100,100],FLIP:(True,False)},
            {TIME: 11*hz,ID: "lober",COL:3, X:150 ,MOV:[60,-30]},
            {TIME: 12*hz,ID: "lober",COL:3, X:-150 ,MOV:[-60,-30]},
            {TIME: 13*hz,ID: "mirror",POS:[100,100],FLIP:(False,True)},
            {TIME: 14*hz,ID: "lober",COL:2, X:150 ,MOV:[60,-30]},
            {TIME: 15*hz,ID: "lober",COL:2, X:-150 ,MOV:[-60,-30]},
            {TIME: 16*hz,ID: "mirror",POS:[100,100],FLIP:(True,False)},
            {TIME: 17*hz,ID: "lober",COL:1, X:150 ,MOV:[60,-30]},
            {TIME: 18*hz,ID: "lober",COL:1, X:-150 ,MOV:[-60,-30]},
            {TIME: 19*hz,ID: "mirror",POS:[100,100],FLIP:(False,True)},
            {TIME: 20*hz,ID: "lober",COL:0, X:150 ,MOV:[60,-30]},
            {TIME: 21*hz,ID: "lober",COL:0, X:-150 ,MOV:[-60,-30]},

            #SPIRAL TRIANGLE
            {TIME: 22*hz,ID: "stay",TILE:[0,1],BREAK:15*hz*fps},{TIME: 22*hz,ID: "stay",TILE:[1,0],BREAK:15*hz*fps},{TIME: 22*hz,ID: "stay",TILE:[0,3],BREAK:15*hz*fps},{TIME: 22*hz,ID: "stay",TILE:[1,4],BREAK:15*hz*fps},{TIME: 22*hz,ID: "stay",TILE:[3,0],BREAK:15*hz*fps},{TIME: 22*hz,ID: "stay",TILE:[4,1],BREAK:15*hz*fps},{TIME: 22*hz,ID: "stay",TILE:[4,3],BREAK:15*hz*fps},{TIME: 22*hz,ID: "stay",TILE:[3,4],BREAK:15*hz*fps},

            {TIME: 23*hz,ID: "return",POS: [300,50] ,MOV:vector_norm([300,50],center,40*1.41),BREAK:25},
            {TIME: 24*hz,ID: "return",ROW:2, Y:50 ,MOV:[0,40],BREAK:25},
            {TIME: 25*hz,ID: "return",POS: [-300,50] ,MOV:vector_norm([-300,50],(-center[0],center[1]),40*1.41),BREAK:25},
            {TIME: 26*hz,ID: "return",COL:2, X:-300 ,MOV:[-40,0],BREAK:25},
            {TIME: 27*hz,ID: "return",POS: [-300,-50] ,MOV:vector_norm([-300,-50],(-center[0],-center[1]),40*1.41),BREAK:25},
            {TIME: 28*hz,ID: "return",ROW:2, Y:-50 ,MOV:[0,-40],BREAK:25},
            {TIME: 29*hz,ID: "return",POS: [300,-50] ,MOV:vector_norm([300,-50],(center[0],-center[1]),40*1.41),BREAK:25},
            {TIME: 30*hz,ID: "return",COL:2, X:300 ,MOV:[40,0],BREAK:25},

            #MUR BOUNCE
            {TIME: 37*hz,ID: "bounce",COL:0, X:50 ,MOV:[10,50]},
            {TIME: 37*hz,ID: "bounce",COL:0, X:146 ,MOV:[10,50]},
            {TIME: 37*hz,ID: "bounce",COL:0, X:242 ,MOV:[10,50]},
            {TIME: 37*hz,ID: "bounce",COL:0, X:338 ,MOV:[10,50]},

            {TIME: 38*hz,ID: "bounce",COL:0, X:-50 ,MOV:[-10,-50]},
            {TIME: 38*hz,ID: "bounce",COL:0, X:-146 ,MOV:[-10,-50]},
            {TIME: 38*hz,ID: "bounce",COL:0, X:-242 ,MOV:[-10,-50]},
            {TIME: 38*hz,ID: "bounce",COL:0, X:-338 ,MOV:[-10,-50]},

            {TIME: 47*hz,ID: "bounce",COL:0, X:-338 ,MOV:[-10,-50]},
            

            ]