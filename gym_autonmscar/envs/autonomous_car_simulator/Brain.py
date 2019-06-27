import time
import pygame

class Brain:
    def __init__(self, database):
        self.database = database

    def run(self):
        while True:
            if self.database.stop:
                break

            time.sleep(0.001)
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
            self.right()
   
            if self.database.car.speed <= 2:
                self.up()
            elif self.database.car.speed > 2:
                self.down()
    
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
