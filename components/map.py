import pygame
TILE_SIZE = 32

#1= wall, 0 = floor
MAP_DATA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class WorldMap:
    def __init__(self):
        self.tiles = []
        for y, row in enumerate(MAP_DATA):
            for x, tile in enumerate(row):
                rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if tile == 1:
                    self.tiles.append(rect)
    def draw(self, surface):
        for rect in self.tiles:
            pygame.draw.rect(surface, (50, 50, 50), rect) #for walls
    def get_collision_rects(self):
        return self.tiles
