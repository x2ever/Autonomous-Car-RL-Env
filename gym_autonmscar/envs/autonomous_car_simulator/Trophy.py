import pygame
import os.path

class TrophySprite(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/images/trophy.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)
