import pygame
from var import *
pygame.init()
spr_cd = pygame.image.load("../sprites/ennemies/cd.png")
spr_maraca = pygame.image.load("../sprites/ennemies/maraca.png")
spr_guitar = pygame.image.load("../sprites/ennemies/guitar.png")
spr_triangle = pygame.image.load("../sprites/ennemies/triangle.png")
spr_radio = pygame.image.load("../sprites/ennemies/radio.png")
spr_mirror = pygame.image.load("../sprites/ennemies/symetrie_cd.png")
spr_blind = pygame.image.load("../sprites/ennemies/blind_cd.png")



class obj_ennemy(pygame.sprite.Sprite): #Création du perso
    def __init__(self): #Les variable du perso
        super().__init__() #Permet de relier un sprite plus tard
        self.id = "stay" #PV du perso
        self.actif = True
        self.waiting = True
        self.grav = 0
        self.mov=[0,0]  #Vélocité du perso [x,y]
        self.angle=0
        self.image= spr_cd #relie le sprite
        self.rect = pygame.Rect((0, 0), (64, 64))
        self.life_time = 0
        self.break_time = 60
        self.reverse = False
        self.damage = True
        self.flip = (False,False)
        self.tiles = [0,0]
        
        
    def draw_ennemy(self,surface):
        launcher = ["rusher", "return"]
        cd_list = ["mirror","blind"]
        cd_size = 80
        
        
        if self.waiting == False:
            self.rect.x, self.rect.y = self.rect.x + self.mov[0] , self.rect.y + self.mov[1]
            if self.id == "rusher":
                self.image = pygame.transform.scale(spr_maraca,(96,96))
                self.angle = (self.angle - (self.mov[0]**2+self.mov[1]**2)**(0.5))%360
            elif self.id == "lober":
                self.grav = 7
                self.image = pygame.transform.scale(spr_guitar,(64,128))
                
                self.mov[1]+= self.grav 
                self.angle = 135 - self.mov[1]
            elif self.id == "return":
                if self.life_time < self.break_time:
                    
                    self.image = pygame.transform.scale(spr_triangle,(96,96))
                    self.angle = get_angle(self.mov) -180
                else:
                    if self.reverse == False:
                        self.mov = (-self.mov[0]*0.5,-self.mov[1]*0.5)
                    self.reverse = True
                    self.image = pygame.transform.scale(spr_triangle,(96,96))
                    self.angle = (self.angle + (self.mov[0]**2+self.mov[1]**2)**(0.5))%360
            elif self.id == "stay":
                self.image = spr_radio
                if self.life_time < self.break_time:
                    self.actif = False
            elif self.id in cd_list:
                self.damage = False
                middle = (screen_size[0]//2-32,screen_size[1]//2-32)
                speed = 0.1
                
                
                self.mov = (speed*(middle[0]-self.rect.x),speed*(middle[1]-self.rect.y))
                self.angle = (self.angle - (self.mov[0]**2+self.mov[1]**2)**(0.5))%360

                if self.id == "mirror":
                    self.image = pygame.transform.scale(spr_mirror,(80,80))
                    
                    if self.life_time < wait-12:
                    
                        pygame.draw.line(surface,(128,255,190),((self.rect.x+32)*self.flip[0],(self.rect.y+32)*self.flip[1]),(self.rect.x + screen_size[0]*int(not(self.flip[0]))+32,self.rect.y +screen_size[1]*int(not(self.flip[1]))+32),3)
                    elif self.life_time < wait:
                        pygame.draw.line(surface,(255,0,0),((self.rect.x+32)*self.flip[0],(self.rect.y+32)*self.flip[1]),(self.rect.x + screen_size[0]*int(not(self.flip[0]))+32,self.rect.y +screen_size[1]*int(not(self.flip[1]))+32),3)
                    else:
                        change_flip(self.flip)
                        self.actif = False
                if self.id == "blind":
                    self.image = pygame.transform.scale(spr_blind,(80,80))
                    if self.life_time > wait:
                        self.actif = False
            

        else:
            self.image= pygame.transform.scale(spr_cd,(cd_size,cd_size))
            self.angle += self.life_time*3
            if self.id in launcher:
                pygame.draw.line(surface,(255,(self.life_time%2)*255,0),(self.rect.x + cd_size//2,self.rect.y + cd_size//2),(self.rect.x + (self.mov[0]*100) + cd_size//2,self.rect.y + (self.mov[1]*100) + cd_size//2),3)
            
            elif self.id == "lober":
                y,x=self.rect.y+32,self.rect.x+32
                y_mov,x_mov=self.mov[1]*(2**(0.5)),self.mov[0]*(2**(0.5))
                for i in range(1,10):
                    x+= x_mov*1.414
                    y+= y_mov
                    y_mov+=7*i
                    pygame.draw.circle(surface,(255,(self.life_time%2)*255,0),(x,y),3)
            elif self.id in cd_list:
                self.waiting = False

        if self.life_time >= wait and self.waiting:
            self.waiting = False

        
        self.life_time+=1
        
        if self.rect.x < 0 or self.rect.x > screen_size[0] or self.rect.y < 0 or self.rect.y > screen_size[1]:
            self.actif = False

        sprite = rotate(self.image,self.rect.topleft,64,self.angle)
        surface.blit(sprite[0],sprite[1])
            
