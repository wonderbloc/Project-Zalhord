import pygame
from var import *

spr_path = pygame.image.load("../sprites/normal_tile.png").convert_alpha()
spr_placeholder = pygame.image.load("../sprites/crane.png").convert_alpha()
spr_craft = pygame.image.load("../sprites/craft_path.png").convert_alpha()
class obj_tile(pygame.sprite.Sprite):
    def __init__(self, id, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.size = 100
        self.amplitude =0
        if self.id == "path":
            self.image = spr_path
        elif self.id == "wall":
            self.image = spr_path
        elif self.id == "mc_path":
            self.image = spr_craft
        # Manual load in: self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center=(self.size//2,self.size//2))
        
        self.rect.x, self.rect.y = x, y

    def draw(self, surface,angle):
        if self.id == "path":
            self.amplitude= max(self.amplitude-(8),0)
            sprite=jiggle(pygame.transform.scale(self.image,(self.size+self.amplitude,self.size+self.amplitude)),self.rect,self.size,angle,5)
            surface.blit(sprite[0], sprite[1])
        else:
            surface.blit(pygame.transform.scale(self.image,(self.size,self.size)),self.rect)
 
class obj_tilemap():
    def __init__(self, mapping):
        self.tile_gap = 120
        self.mc_tile = 100
        self.angle=0
        self.level = mapping[::]
        #self.start_x, self.start_y = 0,0
        self.pos= [0,0]
        self.tiles = self.load_tiles(self.level)
        self.map_table = []
        self.create_map_table()

    def draw_map(self, surface):
        self.angle =(self.angle+0.05)%6.82
        for tile in self.tiles:
            if tile.id != "wall":
                tile.draw(surface,self.angle)

    

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
                            tiles.append(obj_tile("mc_path", self.pos[0] + x * (self.mc_tile),self.pos[1] + y * (self.mc_tile)))
                    x += 1

                # Move to next row
                y += 1
                # Store the size of the tile map
            self.map_w, self.map_h =self.pos[0] + x * self.tile_gap,self.pos[1] + y * self.tile_gap
            if i==0:
                self.pos = [(screen_size[0]//2)-(self.map_w//2),(screen_size[1]//2)-(self.map_h//2)]
        
        
        return tiles
    
    def create_map_table(self):
        for i in range(0, len(self.tiles), len(self.map)):
            line = self.tiles[i:i+len(self.map)]
            self.map_table.append(line)
    

        
            
    def select_tile(self, pos):
        return self.map_table[min(pos[1],len(self.map_table)-1)][min(pos[0],len(self.map_table[-1])-1)]
