import sys 
import pygame

def check_events():
    # monitor the mouse and keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()