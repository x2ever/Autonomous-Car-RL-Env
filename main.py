import time
import threading

from Game import Game 
from Wall import WallSprite
from Car import CarSprite
from Trophy import TrophySprite
from LiDAR import LiDAR
from Brain import Brain


def main():
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
    lidar = LiDAR()
    brain = Brain(lidar, control)
    game = Game(walls, trophies, car, lidar, control)
    game.run()
    while True:
        time.sleep(0.1)
        if game.stop:
            break
    time.sleep(2)
    return 0

if __name__ == "__main__":
    main()