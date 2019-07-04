"""
get play result gif of DQN model
"""

import numpy as np
import gym
import gym_autonmscar
import os
import imageio

from stable_baselines import DQN

model_name = "/dqn/dqn-models/dqn-model_493000.pkl"
gif_file_name = "/dqn-result-gif/atnms-dqn_493000_1.gif"

env = gym.make('autonmscar-v0')
model = DQN.load(os.path.dirname(
    os.path.realpath(__file__)) + model_name)

images = []
done = False
obs = env.reset()
img = env.render(mode='rgb_array')
for i in range(200):
    if done:
        break
    images.append(img)
    action, _ = model.predict(obs)
    obs, _, done, _ = env.step(action)
    img = env.render(mode='rgb_array')  # TODO

imageio.mimsave(os.path.dirname(os.path.realpath(__file__)) +
                gif_file_name, images, duration=0.05)
