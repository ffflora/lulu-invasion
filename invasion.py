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
    ship = Ship(lu_settings,screen)
    # set bgc 
    bg_color = lu_settings.bg_color
    while True:
        # monitor the mouse and keyboard events
        gf.check_events(ship)
        ship.update()
        # show the most recent drawn screen
        gf.update_screen(lu_settings,screen,ship)
        

run_game()
