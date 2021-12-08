import pygame
import sys
import ship

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             sys.exit()
            #  按键事件处理
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=True
            if event.key == pygame.K_LEFT:
                ship.moving_left=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=False
            if event.key == pygame.K_LEFT:
                ship.moving_left=False
  

def update_screen(alien_setting,screen,ship):
    screen.fill(alien_setting.bg_color)
    ship.blitme()
    pygame.display.flip()