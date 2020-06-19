import sys 
import pygame

def check_events(ship):
    # monitor the mouse and keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # press down a key
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP: # don't press a key
            check_keyup_events(event,ship)
         
def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship):
    # show the most recent drawn screen

    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()