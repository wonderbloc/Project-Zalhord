import pygame,csv, os

class obj_grid(pygame.sprite.Sprite):
    def __init__(self, image,x,y,spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        self.rect= self.image.get_rect()
        self.rect.x, self.rect.y = x,y

def draw(self, surface):
    surface.blit(self.image,(self.rect.x,self))

class obj_tilemap():
    def __init__(self, filename, spritesheet):
        self.tile_size = 64
        self.start_x, self.start_y = 0,0
        self.spritesheet = spritesheet

def read_csv(self, filename):
    map = []
    with open(os.path.join(filename)) as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            map.append(list(row))
    return map