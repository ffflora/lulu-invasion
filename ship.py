import pygame


class Ship():

    def __init__(self,lu_settings,screen):

        self.screen = screen 
        self.lu_settings = lu_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() #save the image to a rect
        self.screen_rect = screen.get_rect()
        # put lulu in the middle of the bottm
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # save float type in the `center`
        self.center = float(self.rect.centerx)

        #sign of moving
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.moving_right:
            self.center += self.lu_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.lu_settings.ship_speed_factor
        # update the centerx
        self.rect.centerx = self.center