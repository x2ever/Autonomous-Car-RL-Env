import gym
import gym_autonmscar
import os
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import DQN

env = gym.make('autonmscar-v0')
env = DummyVecEnv([lambda: env])
model = DQN.load(os.path.dirname(
    os.path.realpath(__file__)) + "/test_model.pkl")

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
