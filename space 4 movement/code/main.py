import pygame 
from os.path import join

from random import randint

# general setup 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
running = True
clock = pygame.time.Clock()

# plain surface 
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# imports
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(1,1)
player_speed = 1000

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)) for i in range(20)]

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20,WINDOW_HEIGHT - 20))

while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('darkgray')
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
   
    # player movement
    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0: 
        player_direction.y *= -1
    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction.x *= -1
    player_rect.center += player_direction * player_speed * dt
    display_surface.blit(player_surf, player_rect)

    pygame.display.update()

pygame.quit()