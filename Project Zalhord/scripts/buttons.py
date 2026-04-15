import pygame
from var import *
pygame.init()

spr_b_jouer = pygame.image.load("../sprites/bouton_play.png")
spr_b_pause = pygame.image.load("../sprites/pause.png")
spr_b_level_1 = pygame.image.load("../sprites/level1234.jpg")
spr_b_level_2 = pygame.image.load("../sprites/fond écran png.png")
spr_b_level_3 = pygame.image.load("../sprites/younggirl.jpg")
spr_b_continue = pygame.image.load("../sprites/bouton_continuer.png")

class obj_button(pygame.sprite.Sprite):
    def __init__(self,image, pos,size,action):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.pos = pos
        self.action = action
        self.image = image
        self.size= size
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos[0]*mult, self.pos[1]*mult
    def interact(self):
         if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.action()

    def draw_button(self, surface,mult):
        self.rect.x, self.rect.y = self.pos[0]*mult, self.pos[1]*mult
        self.rect.size = self.size[0]*mult, self.size[1]*mult
        surface.blit(pygame.transform.scale(self.image,(self.size[0],self.size[1])),(self.rect.x//mult,self.rect.y//mult))