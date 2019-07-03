import imageio
import numpy as np
import gym
import gym_autonmscar
import os

from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import DQN

model_name = "/models/dqn-model_544000.pkl"

env = gym.make('autonmscar-v0')
#env = DummyVecEnv([lambda: env])
model = DQN.load(os.path.dirname(
    os.path.realpath(__file__)) + model_name)

images = []
obs = env.reset()
img = env.render(mode='rgb_array')
for i in range(350):
    images.append(img)
    action, _ = model.predict(obs)
    obs, _, _, _ = env.step(action)
    img = env.render(mode='rgb_array')  # TODO

kwargs = {'fps': 29.0}
imageio.mimwrite('autonmscar_dqn.gif', [np.array(
    img[0]) for i, img in enumerate(images) if i % 2 == 0], 'GIF-PIL', **kwargs)
