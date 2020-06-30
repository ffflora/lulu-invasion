import sys 
import pygame
#from bullet import Bullet


def update_screen(settings, screen, ship):
    # redraw the bullets after ship and lulu 
 
    # show the most recent drawn screen
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()

def check_events(ship):
    # monitor the mouse and keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # press down a key
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1

"""         
def check_keydown_events(event, settings, screen, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

        
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

"""