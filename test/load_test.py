import gym
import gym_autonmscar
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import DQN

env = gym.make('autonmscar-v0')
env = DummyVecEnv([lambda: env])
model = DQN.load("test_model.pkl")

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
