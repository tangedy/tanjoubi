import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.rawimage = pygame.image.load('assets/rock.png').convert_alpha()
        self.image = pygame.transform.scale(self.rawimage, (self.rawimage.get_width() * ZOOM, self.rawimage.get_height() * ZOOM))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)