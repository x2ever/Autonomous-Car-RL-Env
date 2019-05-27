#initialize the screen
import pygame, math, sys, time
from pygame.locals import *
from Trophy import TrophySprite
from Car import CarSprite
from Wall import WallSprite
import copy
import math
import cv2
from itertools import chain


class Game:
    def __init__(self, walls, trophies, car, database):
        self.init_args = [copy.copy(walls), copy.copy(trophies), copy.copy(car), database]
        pygame.init()
        self.car = car
        self.screen = pygame.display.set_mode((1024, 768)) 
        self.clock = pygame.time.Clock()
        font = pygame.font.Font(None, 75)
        self.win_font = pygame.font.Font(None, 50)
        self.win_condition = None
        self.win_text = font.render('', True, (0, 255, 0))
        self.loss_text = font.render('', True, (255, 0, 0))
        self.t0 = self.t1 = time.time()
        self.wall_group = pygame.sprite.RenderPlain(*walls)
        self.trophy_group = pygame.sprite.RenderPlain(*trophies)
        self.car_group = pygame.sprite.RenderPlain(car)
        self.rect = self.screen.get_rect()
        self.stop = False
        self.database = database

    def run(self, auto = False):
        while True:
            #USER INPUT
            self.t1 = time.time()
            dt = self.t1-self.t0

            deltat = self.clock.tick(30)
            seconds = round(dt, 2)
            for event in pygame.event.get():
                if auto:
                    if not hasattr(event, 'key'): continue
                    down = event.type == USEREVENT
                    if self.win_condition == None: 
                        if event.key == K_RIGHT: self.car.k_right = down * -5 
                        elif event.key == K_LEFT: self.car.k_left = down * 5
                        elif event.key == K_UP: self.car.k_up = down * 2
                        elif event.key == K_DOWN: self.car.k_down = down * -2 
                        elif event.key == K_ESCAPE: self.database.stop = True
                    elif self.win_condition == True and event.key == K_SPACE:
                        print(seconds)
                        self.database.stop = True
                    elif self.win_condition == False and event.key == K_SPACE:
                        print(seconds)
                        self.again() 
                        self.t0 = self.t1
                    elif event.key == K_ESCAPE:
                        self.database.stop = True
                else:
                    if not hasattr(event, 'key'): continue
                    down = event.type == KEYDOWN 
                    if self.win_condition == None: 
                        if event.key == K_RIGHT: self.car.k_right = down * -5
                        elif event.key == K_LEFT: self.car.k_left = down * 5
                        elif event.key == K_UP: self.car.k_up = down * 2
                        elif event.key == K_DOWN: self.car.k_down = down * -2 
                        elif event.key == K_ESCAPE: self.database.stop = True
                    elif self.win_condition == True and event.key == K_SPACE:
                        print(seconds)
                        self.database.stop = True
                    elif self.win_condition == False and event.key == K_SPACE:
                        print(seconds)
                        self.again() 
                        self.t0 = self.t1
                    elif event.key == K_ESCAPE:
                        self.database.stop = True
            
            if self.database.stop:
                break
                
            #RENDERING
            self.screen.fill((0,0,0))
            self.car_group.update(deltat)
            collisions = pygame.sprite.groupcollide(self.car_group, self.wall_group, False, False, collided = None)
            if collisions != {}:
                self.win_condition = False
                self.car.image = pygame.image.load('images/collision.png')
                loss_text = self.win_font.render('Press Space to Retry', True, (255,0,0))
                seconds = 0
                self.car.MAX_FORWARD_SPEED = 0
                self.car.MAX_REVERSE_SPEED = 0
                self.car.k_right = 0
                self.car.k_left = 0

            trophy_collision = pygame.sprite.groupcollide(self.car_group, self.trophy_group, False, True)
            if trophy_collision != {}:
                seconds = seconds
                self.win_condition = True
                self.car.MAX_FORWARD_SPEED = 0
                self.car.MAX_REVERSE_SPEED = 0
                self.win_text = self.win_font.render('Press Space to Advance', True, (0,255,0))
                if self.win_condition == True:
                    self.car.k_right = -5
                    

            self.wall_group.update(collisions)
            self.wall_group.draw(self.screen)
            self.car_group.draw(self.screen)
            self.trophy_group.draw(self.screen)
            #Counter Render
            self.screen.blit(self.win_text, (250, 700))
            self.screen.blit(self.loss_text, (250, 700))
            pygame.display.flip()
            self.make_lidar_data()
    
    def again(self):
        self.__init__(*self.init_args)
        self.run()

    def make_lidar_data(self):
        L = 70
        array = pygame.surfarray.array3d(self.screen)
        array2 = copy.deepcopy(array)
        car = self.database.car
        x, y = car.position

        car_direction = car.direction % 360

        lidar_x = int(x - 20 * math.sin(math.pi * car_direction / 180))
        lidar_y = int(y - 20 * math.cos(math.pi * car_direction / 180))

        # print(array[lidar_x][lidar_y])

        for direction in range(-90 + car_direction ,90 + car_direction):
            direction = direction % 360
            if 0 < direction < 90:
                direction = 90 -direction
            if 90 < direction < 180:
                direction = 270 - direction
            if 180 < direction < 270:
                direction = 90 - direction
            if 270 < direction < 360:
                direction = 270 - direction
            direction = direction % 360


            x, y = lidar_x, lidar_y
            m = math.tan(math.pi * direction / 180)
            if direction == 0:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x = x
                    y -= 1
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif (0 < direction < 45) or (315 <= direction < 360):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    y -= 1
                    x = (1 / m) * (y - lidar_y) +lidar_x
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif (45 <= direction < 90) or (90 < direction < 135):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x -= 1
                    y = m * (x - lidar_x) +lidar_y
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif direction == 90:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x -= 1
                    y = y
            elif (135 <= direction < 180) or (180 < direction < 225):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    y += 1
                    x = (1 / m) * (y - lidar_y) +lidar_x
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif direction == 180:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x = x
                    y += 1
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif (225 <= direction < 270) or (270 < direction < 315):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L) and (array[int(x)][int(y)] != 255).any():
                    x += 1
                    y = m * (x - lidar_x) +lidar_y
                    try:
                        array[int(x)][int(y)]
                    except IndexError:
                        break
            elif direction == 270:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L) and (array[int(x)][int(y)] != 255).any():
                    x += 1
                    y = y
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            else:
                print(f"Uncatched Case: {direction}")
            try:
                array2[int(x)][int(y)] = [255, 100, 100]
                if array[int(x)][int(y)].all() == 255:
                    print("something")
            except IndexError:
                pass
            l = math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2)
            if l > L:
                l = L
        # print(car_direction - 90, car_direction + 90)
        cv2.imshow('video', array2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()	
            
        

if __name__ == "__main__":
    walls = [
        WallSprite((512, 2.5), 1024, 5),
        WallSprite((512, 765.5), 1024, 5),
        WallSprite((2.5, 384), 5, 768),
        WallSprite((1021.5, 384), 5, 768)
    ]
    trophies = [
        TrophySprite((300,50))
    ]
    car = CarSprite('images/car.png', (50, 700))
    g = Game(walls, trophies, car)
    g.run()

