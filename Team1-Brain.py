import time
import numpy as np
import math
import pygame


class Brain:
    def __init__(self, database):
        self.database = database

    # lidar data [0:179] 반환
    def get_lidar_data(self):
        # lidar값 가져오기
        data = self.database.lidar.data
        return_data = []

        if data is not None:
            data = data.tolist()
            lidar_data = []

            for i in range(360):
                lidar_data.append(data[359 - i])

            DIR = (360 - self.database.car.direction) % 360

            # 1도 인덱스 0, 2도 인덱스 1, ... 360도 인덱스 359
            # print("DIR", DIR)

            for i in range(0, 180):
                return_data.append(lidar_data[(DIR - 90 + i) % 360])
                if i<20:
                    return_data[i]+=5
                if i>160:
                    return_data[i]+=5

            # print(len(return_data),return_data)

        return return_data

    def lidar_cord(self, data):  # data 인덱스 range는 0부터 179까지입니다
        x = 0
        y = 0

        for i in range(90):
            rad = math.radians(i)
            x += data[i] * np.cos(rad)
            y += data[i] * np.sin(rad)

        for i in range(90, 180):
            rad = math.radians(i)
            x += data[i] * np.cos(rad)
            y += data[i] * np.sin(rad)

        return x, y

    def work(self, x, y):
        MAX = 11458.865
        # Hyper parameters
        k = 5

        r = np.sqrt(x ** 2 + y ** 2)
        thetha = int(np.arctan(x / y) * (180 / np.pi))

        if thetha > 5:
            self.left(5)
        elif 0 < thetha <= 5:
            self.left(5)
        elif thetha < -5:
            self.right(5)
        elif -5 <= thetha <= 0:
            self.right(5)
        else:
            pass

        self.down(abs(thetha) // k)

        p = r / MAX
        v = p * 11 // 1
        dv = v - self.database.car.speed
        # print("DV", dv)

        if dv > 3:
            self.up(3)
        elif 0 < dv <= 3:
            self.up(int(dv))
        elif dv < -3:
            self.down(3)
        elif -3 <= dv < 0:
            self.down(int(dv))
        else:
            pass

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

            # Implement Your Algorithm HERE!!

            # EXAMPLE CODE1: 속도 2로 유지하면서 오른쪽으로 회전하기
            # self.right()

            data = self.get_lidar_data()

            if len(data) != 0:
                # print(data)
                x, y = self.lidar_cord(data)
                # print("x", x, "y", y)
                self.work(x, y)

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
