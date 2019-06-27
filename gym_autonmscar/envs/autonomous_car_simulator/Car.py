import pygame
import math
import inspect
import sys
import platform

from Authority import AuthorityExecption


class CarSprite(pygame.sprite.Sprite):
    __MAX_FORWARD_SPEED = 10
    __MAX_REVERSE_SPEED = 10

    def __init__(self, image, position, direction=0):
        pygame.sprite.Sprite.__init__(self)
        self.__src_image = pygame.image.load(image)
        self.__position = position
        self.__speed = 0
        self.__k_left = self.__k_right = self.__k_down = self.__k_up = 0
        self.__direction = direction
        self.update()
    
    def update(self, deltat=False):
        #SIMULATION
        self.__speed += (self.__k_up + self.__k_down)
        if self.__speed > self.__MAX_FORWARD_SPEED:
            self.__speed = self.__MAX_FORWARD_SPEED
        if self.__speed < -self.__MAX_REVERSE_SPEED:
            self.__speed = -self.__MAX_REVERSE_SPEED
        self.__direction += (self.__k_right + self.__k_left)
        x, y = (self.__position)
        rad = self.__direction * math.pi / 180
        x += -self.__speed*math.sin(rad)
        y += -self.__speed*math.cos(rad)
        self.__position = (x, y)
        self.image = pygame.transform.rotate(self.__src_image, self.__direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.__position

    @property
    def MAX_FORWARD_SPEED(self):
        return self.__MAX_FORWARD_SPEED

    @property
    def MAX_REVERSE_SPEED(self):
        return self.__MAX_REVERSE_SPEED
  
    @property
    def speed(self):
        return self.__speed

    @property
    def position(self):
        return self.__position
    
    @property
    def direction(self):
        return self.__direction

    @property
    def k_up(self):
        return self.__k_up

    @property
    def k_down(self):
        return self.__k_down

    @property
    def k_right(self):
        return self.__k_right

    @property
    def k_left(self):
        return self.__k_left

    @k_up.setter
    def k_up(self, new_k_up):
        if platform.system() == 'Windows':
            if inspect.stack()[1][1].split('\\')[-1] == 'Game.py':
                self.__k_up = new_k_up
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.k_up at \'%s\'' % (inspect.stack()[1][1].split('\\')[-1], inspect.stack()[1][0]))   
        else:
            if inspect.stack()[1][1].split('/')[-1] == 'Game.py':
                self.__k_up = new_k_up
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.k_up at \'%s\'' % (inspect.stack()[1][1].split('/')[-1], inspect.stack()[1][0]))   


    @k_down.setter
    def k_down(self, new_k_down):
        if platform.system() == 'Windows':
            if inspect.stack()[1][1].split('\\')[-1] == 'Game.py':
                self.__k_down = new_k_down
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.k_down at \'%s\'' % (inspect.stack()[1][1].split('\\')[-1], inspect.stack()[1][0]))   
        else:
            if inspect.stack()[1][1].split('/')[-1] == 'Game.py':
                self.__k_down = new_k_down
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.k_down at \'%s\'' % (inspect.stack()[1][1].split('/')[-1], inspect.stack()[1][0]))   

    @k_right.setter
    def k_right(self, new_k_right):
        if platform.system() == 'Windows':
            if inspect.stack()[1][1].split('\\')[-1] == 'Game.py':
                self.__k_right = new_k_right
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.k_right at \'%s\'' % (inspect.stack()[1][1].split('\\')[-1], inspect.stack()[1][0]))   
        else:
            if inspect.stack()[1][1].split('/')[-1] == 'Game.py':
                self.__k_right = new_k_right
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.k_right at \'%s\'' % (inspect.stack()[1][1].split('/')[-1], inspect.stack()[1][0]))   

    @k_left.setter
    def k_left(self, new_k_left):
        if platform.system() == 'Windows':
            if inspect.stack()[1][1].split('\\')[-1] == 'Game.py':
                self.__k_left = new_k_left
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.k_left at \'%s\'' % (inspect.stack()[1][1].split('\\')[-1], inspect.stack()[1][0]))   
        else:
            if inspect.stack()[1][1].split('/')[-1] == 'Game.py':
                self.__k_left = new_k_left
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.k_left at \'%s\'' % (inspect.stack()[1][1].split('/')[-1], inspect.stack()[1][0]))   

    @MAX_FORWARD_SPEED.setter
    def MAX_FORWARD_SPEED(self, new_MAX_FORWARD_SPEED):
        if platform.system() == 'Windows':
            if inspect.stack()[1][1].split('\\')[-1] == 'Game.py':
                self.__MAX_FORWARD_SPEED = new_MAX_FORWARD_SPEED
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.MAX_FORWARD_SPEED at \'%s\'' % (inspect.stack()[1][1].split('\\')[-1], inspect.stack()[1][0]))   
        else:
            if inspect.stack()[1][1].split('/')[-1] == 'Game.py':
                self.__MAX_FORWARD_SPEED = new_MAX_FORWARD_SPEED
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.MAX_FORWARD_SPEED at \'%s\'' % (inspect.stack()[1][1].split('/')[-1], inspect.stack()[1][0]))   

    @MAX_REVERSE_SPEED.setter
    def MAX_REVERSE_SPEED(self, new_MAX_REVERSE_SPEED):
        if platform.system() == 'Windows':
            if inspect.stack()[1][1].split('\\')[-1] == 'Game.py':
                self.__MAX_REVERSE_SPEED = new_MAX_REVERSE_SPEED
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.MAX_REVERSE_SPEED at \'%s\'' % (inspect.stack()[1][1].split('\\')[-1], inspect.stack()[1][0]))   
        else:
            if inspect.stack()[1][1].split('/')[-1] == 'Game.py':
                self.__MAX_REVERSE_SPEED = new_MAX_REVERSE_SPEED
            else:
                sys.tracebacklimit = 0
                print("YOU ARE TRYING TO CHEAT!")
                raise AuthorityExecption('Not allowed File %s is trying to change CarSprite.MAX_REVERSE_SPEED at \'%s\'' % (inspect.stack()[1][1].split('/')[-1], inspect.stack()[1][0]))   
