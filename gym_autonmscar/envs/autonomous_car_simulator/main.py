import time
import pygame
import threading
import argparse
import os


from gym_autonmscar.envs.autonomous_car_simulator.Game import Game
from gym_autonmscar.envs.autonomous_car_simulator.Wall import WallSprite
from gym_autonmscar.envs.autonomous_car_simulator.Car import CarSprite
from gym_autonmscar.envs.autonomous_car_simulator.Trophy import TrophySprite
from gym_autonmscar.envs.autonomous_car_simulator.LiDAR import LiDAR
from gym_autonmscar.envs.autonomous_car_simulator.Brain import Brain
from gym_autonmscar.envs.autonomous_car_simulator.Control import Control
from gym_autonmscar.envs.autonomous_car_simulator.Database import Database
from gym_autonmscar.envs.autonomous_car_simulator.Course import Map1, Map2, Map3


def main(auto):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 30)
    walls, trophies, car = Map1
    lidar = LiDAR()
    control = Control()
    database = Database(lidar, control, car)
    brain = Brain(database)  # Get LiDAR data, Set Control data
    # Get Control data Set LiDAR data
    game = Game(walls, trophies, car, database)
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
