import gym
import gym_autonmscar
import os
from stable_baselines import DDPG

# TODO: use argparse
model_name = "/ddpg-models/ddpg-model_3000.pkl"

env = gym.make('autonmscarContinuous-v0')
model = DDPG.load(os.path.dirname(
    os.path.realpath(__file__)) + model_name)

obs = env.reset()
done = False
for i in range(1000):
    if done:
        env.reset()
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
