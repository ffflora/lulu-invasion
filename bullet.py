import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,lu_settings, screen, ship):
        # create the bullet
        super().__init__()
        self.screen = screen 

        # create a rect for bullet 
        self.rect = pygame.Rect(0,0,lu_settings.bullet_width,
            lu_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # save the location as floating points
        self.y = float(self.rect.y)
        self.color = lu_settings.bullet_color
        self.speed_factor = lu_settings.bullet_speed_factor