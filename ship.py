import pygame


class Ship():

    def __init__(self,screen):
        self.screen = screen 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() #save the image to a rect
        self.screen_rect = screen.get_rect()
        # put lulu in the middle of the bottm
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)