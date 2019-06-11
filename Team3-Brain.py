import time
import pygame
import numpy as np

class Brain:
    def __init__(self, database):
        self.database = database

    def run(self):
        start = False
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
                self.left(num)a?
                self.database.car.direction
                self.database.car.speed

                ☆☆☆☆☆ In one loop, you can only change the speed up to 3 and the angle up to 5!!

            3. How can i get a car status dat
            '''
            if self.database.lidar.data is not None:
                start = True
            if start:
                data = self.database.lidar.data
                car_dir = self.database.car.direction
                if car_dir ==45:
                    car_dir -=1
                if car_dir ==-225:
                    car_dir +=1
                if car_dir == -180:
                    car_dir +=1
                car_dirq = car_dir - 90
                car_dirw = car_dir - 45
                car_dire = car_dir + 45
                car_dirr = car_dir + 87
                RRD = np.array(data[car_dirq])
                RD = np.array(data[car_dirw])
                D = np.array(data[car_dir])
                LD = np.array(data[car_dire])
                LLD = np.array(data[car_dirr])
                print(car_dir)
                if RD<40 :
                    self.left(5)

                if LD<40 :
                    self.right(5)

                if 40<RD<70 :
                    self.left(4)

                if 40<LD<70 :
                    self.right(4)

                if RD == 100 :

                    if self.database.car.speed <= 2:
                        self.up(2)
                    elif self.database.car.speed > 2:
                        self.down(2)
                    self.right(5)
                if LD == 100 :

                    if self.database.car.speed <= 2:
                        self.up(2)
                    elif self.database.car.speed > 2:
                        self.down(2)
                    self.left(5)
                if RRD == 100 :

                    if self.database.car.speed <= 1:
                        self.up(3)
                    elif self.database.car.speed > 1:
                        self.down(3)
                    self.right(5)
                if LLD == 100 :

                    if self.database.car.speed <= 1:
                        self.up(3)
                    elif self.database.car.speed > 1:
                        self.down(3)
                    self.left(5)
                if D==100:
                    if self.database.car.speed <= 10:
                        self.up(3)
                    elif self.database.car.speed > 10:
                        self.down(3)


                # Implement Your Algorithm HERE!!

                # EXAMPLE CODE1: 속도 2로 유지하면서 오른쪽으로 회전하기
                '''self.left()'''

                '''if self.database.car.speed <= 2:
                    self.up()git
                elif self.database.car.speed > 2:
                    self.down()'''

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

