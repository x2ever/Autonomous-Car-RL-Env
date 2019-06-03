import time
import pygame
import threading
import argparse
import os


from Game import Game 
from Wall import WallSprite
from Car import CarSprite
from Trophy import TrophySprite
from LiDAR import LiDAR
from Brain import Brain
from Control import Control
from Database import Database
from Course import Map1, Map2, Map3

def main(auto):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 30)
    walls, trophies, car = Map1
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