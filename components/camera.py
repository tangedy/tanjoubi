import pygame
class Cameraclass:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.offset = pygame.Vector2()
    def update(self, target):
        self.offset.x = target.rect.centerx - self.width // 2
        self.offset.y = target.rect.centery - self.height // 2
    def get_rect(self):
        return pygame.Rect(self.offset.x, self.offset.y, self.width, self.height)

