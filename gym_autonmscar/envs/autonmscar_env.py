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

    continuous = False

    def __init__(self):
        # change the map version using this value (0, 1, 2)
        self._map_version = 0
        # initialize the RL environment
        if self.continuous:
            # the probability of up, down, left, right, respectively
            self.action_space = spaces.Box(low=-1, high=1, shape=(4, ))
        else:
            self.action_space = spaces.Discrete(4)  # up, down, left, right
        L = 100  # in LiDAR.py
        # (360 for LiDAR data) + (3 for the status of car)
        self.observation_size = 360 + 3
        self.observation_space = spaces.Box(
            low=0, high=L, shape=(self.observation_size,))

    def step(self, action):
        if self.continuous:
            action = softmax(action)
            action = np.random.choice(4, 1, p=action)
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

        # rewards
        reward = 0
        if self.game.win_condition == False:  # when colliding the wall
            # print("Fail")
            reward -= 10
        elif self.game.win_condition == True:  # when getting the trophy
            print("Success, result: " + result)
            reward += 100 / result + 1000
        else:  # moving is the reward
            # speed range: -10 to 10
            reward += self.game.car.speed
            if self.game.car.speed == 0:
                reward = -1

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
        if self._map_version == 1:
            walls, trophies, car = Map1
            # for deepcopy...
            car = CarSprite(
                './gym_autonmscar/envs/autonomous_car_simulator/images/car.png', (50, 700))
        elif self._map_version == 2:
            walls, trophies, car = Map2
            car = CarSprite(
                './gym_autonmscar/envs/autonomous_car_simulator/images/car.png', (50, 700))
        else:
            walls, trophies, car = Map3
            car = CarSprite(
                './gym_autonmscar/envs/autonomous_car_simulator/images/car.png', (30, 570), -20)

        self.database = Database(lidar, control, car)
        self.game = Game(walls, trophies, car, self.database)
        self.game.seconds = 0
        self.game.record = False

        obs = self.game.make_obs()
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


class AutonomousCarEnvContinuous(AutonomousCarEnv):
    continuous = True


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
