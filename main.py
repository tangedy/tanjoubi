import pygame
from components.player import Playerclass
from components.camera import Cameraclass
import sys
from components.map import WorldMap
pygame.init()

#SCREEN SETTINGS
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
zoom = 1.7
#game settings
map_width, map_height = 1600, 1200
world = pygame.Surface((map_width, map_height))
game_map = WorldMap()


#fonts and colors
font = pygame.font.SysFont('Comic Sans MS', 24
)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#player and camera
player = Playerclass(400, 300)
camera = Cameraclass(WIDTH, HEIGHT, 2)
camera.set_world_size(map_width, map_height)

#MAIN LOOP
running = True
while running:
    dt = clock.tick(60) / 1000 #delta time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.update(game_map.get_collision_rects())
    camera.update(player)
    world.fill((100, 200, 255))
    player.draw(world)
    game_map.draw(world)

    #blit visible part of world to screen using camera offset
    camera_rect = camera.get_rect()
    scaled_view = pygame.transform.scale(world.subsurface(camera_rect), (WIDTH, HEIGHT))
    screen.blit(scaled_view, (0, 0))
    pygame.display.update()
pygame.quit()