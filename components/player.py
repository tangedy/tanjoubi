import pygame
class Playerclass:
    def __init__(self, x, y):
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 200
    def update(self, collisions):
        keys = pygame.key.get_pressed()
        dx = dy = 0

        for rect in collisions:
            if self.rect.colliderect(rect):
                if dx > 0: 
                    self.rect.right = rect.left
                elif dx < 0: 
                    self.rect.left = rect.right
        for rect in collisions:
            if self.rect.colliderect(rect):
                if dy > 0: 
                    self.rect.top = rect.bottom
                elif dy < 0: 
                    self.rect.bottom = rect.top

                    
        if keys[pygame.K_LEFT]: dx -= 1
        if keys[pygame.K_RIGHT]: dx += 1
        if keys[pygame.K_UP]: dy += 1
        if keys[pygame.K_DOWN]: dy -= 1
        dx *= self.speed * 0.016
        dy *= self.speed * 0.016

        self.rect.y += dy
        for rect in collisions:
            if self.rect.colliderect(rect):
                if dy > 0: 
                    self.rect.top = rect.bottom
                elif dy < 0: 
                    self.rect.bottom = rect.top
                    
        self.rect.x += dx
        for rect in collisions:
            if self.rect.colliderect(rect):
                if dx > 0: 
                    self.rect.right = rect.left
                elif dx < 0: 
                    self.rect.left = rect.right

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
    