import sys 
import pygame
from bullet import Bullet

def check_events(settings, screen, ship, bullets):
    # monitor the mouse and keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # press down a key
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP: # don't press a key
            check_keyup_events(event, ship)
         
def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
        
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship, bullets):
    # redraw the bullets after ship and lulu 
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # show the most recent drawn screen
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()