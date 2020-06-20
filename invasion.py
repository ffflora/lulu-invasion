import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import functions as gf



def run_game():
    pygame.init()
    lu_settings = Settings()
    screen = pygame.display.set_mode((lu_settings.screen_width, lu_settings.screen_height))
    pygame.display.set_caption("lulu Invasion")
    
    # Init a ship
    ship = Ship(lu_settings, screen)

    # Create an arr to store the bullets
    bullets = Group()

    # set bgc 
    

    while True:
        # monitor the mouse and keyboard events
        gf.check_events(lu_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # show the most recent drawn screen
        gf.update_screen(lu_settings, screen, ship, bullets)
        

run_game()
