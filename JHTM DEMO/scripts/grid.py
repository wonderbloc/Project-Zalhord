import pygame

class obj_grid(pygame.sprite.Sprite):
    def __init__(self, image,x,y,spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.rect= self.image.get_rect()
        self.rect.x, self.rect.y = x,y

def draw(self, surface):
    surface.blit(self.image,(self.rect.x,self))

class obj_tilemap():
    def __init__(self,list , spritesheet):
        self.tile_size = 64
        self.start_x, self.start_y = 0,0
        self.spritesheet = spritesheet
        self.tiles =self.load_tiles(list)
        self.map_surface = pygame.Surface((self.map_w,self.map_h))
        self.map_surface.set_colorkey((0,0,0))

def load_map(self): 
    for tile in self.tiles:
        tile.draw(self.map_surface)
def load_tiles(self,list):
    tiles=[]
    x,y=0,0
    for row in list:
        x=0
        for tile in row:
            if tile == 0:
                pass
            elif tile == 1:
                tiles.append(obj_grid,x*64,y*64)
            x+=1
        y+=1
