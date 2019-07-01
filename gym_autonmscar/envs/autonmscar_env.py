import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import pygame
import os

from gym_autonmscar.envs.autonomous_car_simulator.Brain import Brain
from gym_autonmscar.envs.autonomous_car_simulator.LiDAR import LiDAR
from gym_autonmscar.envs.autonomous_car_simulator.Control import Control
from gym_autonmscar.envs.autonomous_car_simulator.Course import Map1, Map2, Map3
from gym_autonmscar.envs.autonomous_car_simulator.Database import Database
from gym_autonmscar.envs.autonomous_car_simulator.Game import Game
from gym_autonmscar.envs.autonomous_car_simulator.Car import CarSprite


class AutonomousCarEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # initialize the RL environment
        self.action_space = spaces.Discrete(4)  # up, down, left, right
        L = 100  # in LiDAR.py
        # (360 for LiDAR data) + (2 for the status of car)
        self.observation_size = 360 + 2
        self.observation_space = spaces.Box(
            low=0, high=L, shape=(self.observation_size,))

    def step(self, action):
        if self.game.win_condition is not None:
            self.finish()
        else:
            if action == 0:
                self.up()
            elif action == 1:
                self.down()
            elif action == 2:
                self.right()
            elif action == 3:
                self.left()
        obs, result = self.game.step()
        # TODO: reward?
        reward = 0
        if self.game.win_condition == False:
            print("Fail")
            reward -= 1
        elif self.game.win_condition == True:
            print("Success, result: " + result)
            reward += 100 / result + 1000
        else:
            # speed range: 0 - 10
            reward += self.game.car.speed

        return obs, reward, self.database.stop, {}

    def reset(self):
        try:
            del self.game
            del self.database
            pygame.event.get()
        except:
            pass
        # initialize the game
        lidar = LiDAR()
        control = Control()
        walls, trophies, car = Map1
        # for deepcopy...
        car = CarSprite(
            './gym_autonmscar/envs/autonomous_car_simulator/images/car.png', (50, 700))
        self.database = Database(lidar, control, car)
        self.game = Game(walls, trophies, car, self.database)
        self.game.seconds = 0
        self.game.record = False

        # TODO: can be a module
        self.game.make_lidar_data()
        obs = np.insert(self.database.lidar.data, -1, self.game.car.direction)
        obs = np.insert(obs, -1, self.game.car.speed)

        return obs

    def render(self, mode='human', close=False):
        self.game.render()

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

    def finish(self):
        self.database.control.finish()
