import pygame

class spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()

    def parse_sprite(self, rect):
        image = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        return image

class obj_tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.tile_size = 80
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.tile_size,self.tile_size))
        # Manual load in: self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
 
class obj_tilemap():
    def __init__(self, mapping):
        self.tile_gap = 90
        self.start_x, self.start_y = 0,0
        self.pos=[0,0]
        self.tiles = self.load_tiles(mapping)

    def draw_map(self, surface):
        for tile in self.tiles:
            tile.draw(surface)

    

    def load_tiles(self, mapping):
        tiles = []
        map = mapping
        x, y = 0,0, 
        for row in map:
            x = 0
            for tile in row:
                if tile == 0:
                    self.start_x, self.start_y =self.start_x+ x * self.tile_gap,self.start_y+ y * self.tile_gap
                    tiles.append(obj_tile('sprites/crane.png',self.pos[0]+ x * (self.tile_gap), self.pos[0]+y * (self.tile_gap)))
                elif tile == 1:
                    tiles.append(obj_tile('sprites/normal_tile.png', self.pos[0] + x * (self.tile_gap),self.pos[0] + y * (self.tile_gap)))
                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_gap, y * self.tile_gap
        return tiles
    

        
            


    def select_tile(self, pos):
        self.select = self.map_w * (pos[1]-1) + pos[0]
        return self.tiles[0]
