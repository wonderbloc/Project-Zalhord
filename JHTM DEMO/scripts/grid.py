import pygame
from var import *

spr_path = pygame.image.load("sprites/normal_tile.png").convert_alpha()
spr_glass = pygame.image.load("sprites/glass_tile.png").convert_alpha()
spr_placeholder = pygame.image.load("sprites/crane.png").convert_alpha()
class obj_tile(pygame.sprite.Sprite):
    def __init__(self, id, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.size = 100
        if self.id == "path":
            self.image = spr_path
        elif self.id == "glass":
            self.image = spr_glass
        elif self.id == "wall":
            self.image = spr_path

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
                            tiles.append(obj_tile("wall",self.pos[0]+ x * (self.tile_gap), self.pos[1]+y * (self.tile_gap)))
                        elif tile == 1:
                            tiles.append(obj_tile("path", self.pos[0] + x * (self.tile_gap),self.pos[1] + y * (self.tile_gap)))
                        elif tile == 2:
                            tiles.append(obj_tile("glass", self.pos[0] + x * (self.tile_gap),self.pos[1] + y * (self.tile_gap)))
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
