import time
import pygame
import numpy as np
import math


class Brain:
    def __init__(self, database):
        self.database = database

    def sigmoid(self, x):
        return 8 * (1 / (1 + np.exp(-x)) - 0.5)

    def run(self):
        while True:
            if self.database.stop:
                break
            time.sleep(0.01)
            events = pygame.event.get()

            '''
            DO NOT CHANGE CODE ABOVE!!!!
            '''

            ''' 
            1. How can i get a lidar data?
                data = self.database.lidar.data

            2. How can i move a car?
                self.database.control.up()
                self.database.control.down()
                self.database.control.right()
                self.database.control.left()

                OR

                self.up(num)
                self.down(num)
                self.right(num)
                self.left(num)

                ☆☆☆☆☆ In one loop, you can only change the speed up to 3 and the angle up to 5!!

            3. How can i get a car status data?
                self.database.car.direction
                self.database.car.speed
            '''
            data = self.database.lidar.data
            X = np.linspace(0, 360, 360)
            Y = np.linspace(0, 360, 360)
            rtot = 180 / math.pi

            if data is not None:
                BOOL = data < 50
                data = data - BOOL * data
                BOOL = data > 90
                data = data + BOOL * data * 1.6
                BOOL = data > 95
                data = data + BOOL * data*1.8

                X[:] = data[:] * np.cos(Y * np.pi / 180)
                Y[:] = data[:] * np.sin(Y * np.pi / 180)

                x = np.sum(X)
                y = np.sum(Y)

                angle = round(np.arctan2(y, x) * rtot)
                angle = -(self.database.car.direction - angle)

                while angle <= 0:
                    angle += 360
                if angle > 180:
                    angle -= 360
                angle = int(angle)
                if angle > 0:
                    if angle > 4:
                        self.left(5)
                    else:
                        self.left(angle)
                else:
                    if angle < -4:
                        self.right(5)
                    else:
                        self.right(-angle)

                tovel = 10 - (abs(angle)) / 5
                accel = int(round(self.sigmoid((tovel - self.database.car.speed + 1))))
                if accel > 0:
                    self.up(min(accel, 3))
                else:
                    self.down(min(-accel, 3))

    def up(self, num: int = 1):
        for i in range(num):
            self.database.control.up()

    def down(self, num: int = 1):
        for i in range(num):
            self.database.control.down()

    def right(self, num: int = 1):
        for i in range(num):
            self.database.control.right()

    def left(self, num: int = 1):
        for i in range(num):
            self.database.control.left()