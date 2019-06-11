import time
import pygame
import numpy as np

class Brain:
 def __init__(self, database):
     self.database = database

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

         data = self.database.lidar.data
         threshold = 45
         if(data is not None):
             car_dir = self.database.car.direction
             if(car_dir<0):
                 car_dir+=360
             L = data[(89+car_dir)%360]
             R = data[(271+car_dir)%360]
             F = data[car_dir]
             FL = data[(49+car_dir)%360]
             FR = data[(311+car_dir)%360]
             prior = [L, R, FL, FR, F]

             if (F < 30 or FR < 50 or FL < 50):
                 self.down(3)

             if F<85:
                 if self.database.car.speed > 4:
                     self.down(3)

             if (np.argmax(prior) == 4): # F일 때
                 self.up(3)
                 if FL<threshold or L<threshold:
                     self.right(5)
                     self.up()
                 elif FR<threshold or R<threshold:
                     self.left(5)
                     self.up()

             elif (np.argmax(prior) == 1): # R일 때
                 self.right(5)
                 self.right(5)
                 self.right(5)
                 self.right(5)
                 self.right(5)
                 self.right(5)
                 self.right(5)
                 self.right(5)
                 if FL<threshold or L<threshold:
                     self.right(5)
                     self.right(5)

             elif (np.argmax(prior) == 0): #L일 때
                 self.left(5)
                 self.left(5)
                 self.left(5)
                 self.left(5)
                 self.left(5)
                 self.left(5)
                 self.left(5)
                 self.left(5)
                 if FL<threshold or L<threshold:
                     self.right(5)
                     self.right(5)
                 elif FR<threshold or R<threshold:
                     self.left(5)
                     self.left(5)

             elif (np.argmax(prior) == 3): #FR일 때
                 self.up()
                 self.right(5)
                 self.right(5)
                 self.right(5)
                 self.right(5)
                 self.right(5)
                 self.right(5)
                 if FL<threshold or L<threshold:
                     self.right(5)
                     self.right(5)
                     self.right(5)
                     self.right(5)
                     self.right(5)
                     self.right(5)
                 if self.database.car.speed < 3:
                     self.up(3)
                     self.up()


             elif (np.argmax(prior) == 2): # FL일 때
                 self.up()
                 self.left(5)
                 self.left(5)
                 self.left(5)
                 self.left(5)
                 self.left(5)
                 self.left(5)
                 if FR<threshold or R<threshold:
                     self.left(5)
                     self.left(5)
                     self.left(5)
                     self.left(5)
                     self.left(5)
                     self.left(5)
                 if self.database.car.speed < 3:
                     self.up(3)
                     self.up()

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






