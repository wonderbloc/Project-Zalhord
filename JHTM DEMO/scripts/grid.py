import pygame
from var import *

class spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()

    def parse_sprite(self, rect):
        image = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        return image

class obj_tile(pygame.sprite.Sprite):
    def __init__(self, image, id, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.size = 100
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        # Manual load in: self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
 
class obj_tilemap():
    def __init__(self, mapping,start,window_size):
        self.start_pos=start
        self.tile_gap = 120
        self.window_size=window_size
        #self.start_x, self.start_y = 0,0
        self.pos= [0,0]
        self.tiles = self.load_tiles(mapping)
        self.map_table = []

    def draw_map(self, surface):
        for tile in self.tiles:
            if tile.id != "wall":
                tile.draw(surface)

    

    def load_tiles(self, mapping):
        tiles = []
        self.map = mapping
        
        for i in range(2):
            x, y = 0,0 
            for row in self.map:
                x = 0
                for tile in row:
                    if i == 1:
                        if tile == 0:
                        # self.start_x, self.start_y =self.start_x+ x * self.tile_gap,self.start_y+ y * self.tile_gap
                            tiles.append(obj_tile('sprites/crane.png',"wall",self.pos[0]+ x * (self.tile_gap), self.pos[1]+y * (self.tile_gap)))
                        elif tile == 1:
                            tiles.append(obj_tile('sprites/normal_tile.png',"path", self.pos[0] + x * (self.tile_gap),self.pos[1] + y * (self.tile_gap)))
                    x += 1

                # Move to next row
                y += 1
                # Store the size of the tile map
            self.map_w, self.map_h =self.pos[0] + x * self.tile_gap,self.pos[1] + y * self.tile_gap
            if i==0:
                self.pos = [(self.window_size[0]//2)-(self.map_w//2),(self.window_size[1]//2)-(self.map_h//2)]

        return tiles
    
    

        
            
    def select_tile(self, pos):
        
        
        for i in range(0, len(self.tiles), len(self.map)):
            line = self.tiles[i:i+len(self.map)]
            self.map_table.append(line)
        return self.map_table[min(pos[1],len(self.map_table)-1)][min(pos[0],len(self.map_table[-1])-1)]
