import time
import pygame
import threading
import argparse

from Game import Game 
from Wall import WallSprite
from Car import CarSprite
from Trophy import TrophySprite
from LiDAR import LiDAR
from Brain import Brain
from Control import Control
from Database import Database

def main(auto):
    walls = [
        WallSprite((512, 2.5), 1024, 5),
        WallSprite((512, 765.5), 1024, 5),
        WallSprite((2.5, 384), 5, 768),
        WallSprite((1021.5, 384), 5, 768),
        WallSprite((113 * 1, 768 - 130), 5, 260),
        WallSprite((113 * 2, 768 - 230), 5, 260),
        WallSprite((113 * 3, 768 - 130), 5, 260),
        WallSprite((113 * 4, 768 - 230), 5, 260),
        WallSprite((113 * 5, 768 - 130), 5, 260),
        WallSprite((113 * 6, 768 - 230), 5, 260),
        WallSprite((113 * 7, 768 - 130), 5, 260),
        WallSprite((113 * 8, 768 - 230), 5, 260),
        WallSprite((113 * 4, 768 - 360), 113 * 8, 5),
        WallSprite((1024 - 113 * 4, 768 - 490), 113 * 8, 5),
        WallSprite((1024 - 113 * 4, 130), 113 * 8, 5),
        WallSprite((120 , 204), 5, 152),
    ]
    trophies = [
        TrophySprite((950,45))
    ]
    car = CarSprite('images/car.png', (50, 700))
    lidar = LiDAR()
    control = Control()
    database = Database(lidar, control, car)
    brain = Brain(database) # Get LiDAR data, Set Control data
    game = Game(walls, trophies, car, database) # Get Control data Set LiDAR data
    if auto:
        brain_thread = threading.Thread(target=brain.run,)
        brain_thread.start()

    game.run(auto=auto)
    pygame.quit()

    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--auto", help="Do not use your keyboard command, but use pre-defined brain's command.",
                    action="store_true", default=False)
    args = parser.parse_args()
    main(args.auto)