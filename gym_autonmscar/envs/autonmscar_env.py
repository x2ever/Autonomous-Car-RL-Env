import gym
from gym import error, spaces, utils
from gym.utils import seeding

from gym_autonmscar.envs.autonomous_car_simulator.Brain import Brain


class AutonomousCarEnv(gym.Env, Brain):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(4)  # up, down, left, right

        L = 100  # in LiDAR.py
        # (360 for LiDAR data) + (2 for the status of car)
        self.observation_size = self.database.lidar.data.shape[0] + 2
        self.observation_space = spaces.Box(
            low=0, high=L, shape=(self.observation_size, 0))

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pass
