import pygame
from settings import Settings
from ship import Ship
import functions as gf

def run_game():
    pygame.init()
    lu_settings = Settings()
    screen = pygame.display.set_mode((lu_settings.screen_width,lu_settings.screen_height))
    pygame.display.set_caption("lulu Invasion")
    
    # Init a ship
    ship = Ship(screen)
    # set bgc 
    bg_color = lu_settings.bg_color
    while True:
        # monitor the mouse and keyboard events
        gf.check_events()
        # show the most recent drawn screen
        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()

run_game()
