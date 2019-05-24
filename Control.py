import pygame
from pygame.locals import *
class Control:
    def __init__(self):
        self.up_event = pygame.event.Event(pygame.USEREVENT, {'key': K_UP})
        self.down_event = pygame.event.Event(pygame.USEREVENT, {'key': K_DOWN})
        self.right_event = pygame.event.Event(pygame.USEREVENT, {'key': K_RIGHT})
        self.left_event = pygame.event.Event(pygame.USEREVENT, {'key': K_LEFT})
    
    def up(self):
        pygame.event.post(self.up_event)
    
    def down(self):
        pygame.event.post(self.down_event)

    def right(self):
        pygame.event.post(self.right_event)
    
    def left(self):
        pygame.event.post(self.left_event)