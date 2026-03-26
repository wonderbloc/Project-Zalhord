import pygame

class spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()

    def parse_sprite(self, rect):
        image = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        return image

class obj_grid(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        # Manual load in: self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class obj_tilemap():
    def __init__(self, mapping):
        self.tile_size = 64
        self.tile_gap = 10
        self.start_x, self.start_y = 0, 0
        self.tiles = self.load_tiles(mapping)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def draw_map(self, surface,pos):
        surface.blit(self.map_surface, pos)

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def load_tiles(self, mapping):
        tiles = []
        map = mapping
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == 0:
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif tile == 1:
                    tiles.append(obj_grid('sprites/1_tile.png', x * (self.tile_size+self.tile_gap), y * (self.tile_size+self.tile_gap)))
                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
