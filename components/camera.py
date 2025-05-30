import pygame
class Cameraclass:
    def __init__(self, width, height, zoom =2):
        self.width = width // zoom
        self.height = height // zoom
        self.offset = pygame.Vector2()
        self.world_width = 1600
        self.world_height = 1200
    def update(self, target):
        self.offset.x = target.rect.centerx - self.width // 2
        self.offset.y = target.rect.centery - self.height // 2

        #clamp to world bounds
        self.offset.x = max(0, min(self.offset.x, self.world_width - self.width))
        self.offset.y = max(0, min(self.offset.y, self.world_height - self.height))

    def get_rect(self):
        return pygame.Rect(self.offset.x, self.offset.y, self.width, self.height)
    
    def set_world_size(self, width, height):
        self.world_width = width
        self.world_height = height
