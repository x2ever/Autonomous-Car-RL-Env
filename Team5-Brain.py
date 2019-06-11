import time
import pygame
import numpy as np

class Brain:
    def __init__(self, database):
        self.database = database
        self.previous_front = int()
        self.previous_left = int()
        self.previous_right = int()
        self.next_turn = str()
        self.data = np.zeros((360))

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

            
            if self.database.lidar.data is not None:
                self.data = np.where(self.database.lidar.data==0, 999, self.database.lidar.data)
                front = self.get_front_distance(self.database.car.direction)
                left = self.get_left_distance(self.database.car.direction)
                right = self.get_right_distance(self.database.car.direction)

                # Fix the 'Zero Bug'
                if left == 0:
                    left = self.previous_left
                if right == 0:
                    right = self.previous_right
                
                if self.is_danger():
                    if self.database.car.speed > -1:
                        self.down(2)
                    else:
                        self.up(1)
                else:
                    if front < 70 or left < 30 or right < 30:
                        if self.database.car.speed > 4:
                            self.down(3)
                        elif self.database.car.speed == 4:
                            self.down(1)
                            
                        if self.next_turn == "LEFT" and self.get_left_min_distance(self.database.car.direction) > 45:
                            self.left(5)
                        elif self.get_left_min_distance(self.database.car.direction) <= 45:
                            self.right(5)
                            self.next_turn = "RIGHT"
                        elif self.next_turn == "RIGHT" and self.get_right_min_distance(self.database.car.direction) > 45:
                            self.right(5)
                        elif self.get_right_min_distance(self.database.car.direction) <= 45:
                            self.left(5)
                            self.next_turn = "LEFT"
                    else:
                        self.up(3)
                    
                    if left - self.previous_left > 25:
                        self.next_turn = "LEFT"
                    if right - self.previous_right > 25:
                        self.next_turn = "RIGHT"
                        
                self.previous_front = front
                self.previous_left = left
                self.previous_right = right
    
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

    def is_danger(self):
        if self.data.min() < 20:
            return True
        return False
    
    def get_front_distance(self, direction):
        min_distance = 100
        direction = direction % 360
        for d in range(direction - 35, direction + 35):
            d = d % 360
            if self.data[d] == 999:
                continue
            if min_distance > self.data[d]:
                min_distance = self.data[d]
        return min_distance

    def get_left_min_distance(self, direction):
        min_distance = 100
        direction = direction % 360
        for d in range(direction + 45, direction + 90):
            d = d % 360
            if self.data[d] == 999:
                continue
            if min_distance > self.data[d]:
                min_distance = self.data[d]
        return min_distance
    
    def get_right_min_distance(self, direction):
        min_distance = 100
        direction = direction % 360
        for d in range(direction - 90, direction - 45):
            d = d % 360
            if self.data[d] == 999:
                continue
            if min_distance > self.data[d]:
                min_distance = self.data[d]
        return min_distance

    def get_left_distance(self, direction):
        max_distance = 0
        direction = direction % 360
        for d in range(direction + 88, direction + 89):
            d = d % 360
            if self.data[d] == 999:
                continue
            if max_distance < self.data[d]:
                max_distance = self.data[d]
        return max_distance
    
    def get_right_distance(self, direction):
        max_distance = 0
        direction = direction % 360
        for d in range(direction - 89, direction - 88):
            d = d % 360
            if self.data[d] == 999:
                continue
            if max_distance < self.data[d]:
                max_distance = self.data[d]
        return max_distance