from settings import *
import pygame
from tile import Tile
from player import Player
from debug import Debug
class Level:
    def __init__(self):
        #get the display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        #sprite setp
        self.create_map()
    
    def create_map(self):
        for row_index, row in enumerate(world_map):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
            
                if col == 1:
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 2:
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)



    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw()
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)
        
