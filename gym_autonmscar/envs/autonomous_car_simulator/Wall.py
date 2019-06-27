import pygame
import numpy as np
import os.path

class WallSprite(pygame.sprite.Sprite):
    hit = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/images/collision.png')
    def __init__(self, position, width, height):
        super(WallSprite, self).__init__()
        black_wall = 255 * np.ones((width, height, 3))
        self.normal = pygame.surfarray.make_surface(black_wall)
        self.rect = pygame.Rect(self.normal.get_rect())
        self.rect.center = position

    def update(self, hit_list):
        if self in hit_list: self.image = self.hit
        else: self.image = self.normal

if __name__ == "__main__":
    pygame.init()
    w = WallSprite((10,2), 1, 1)
