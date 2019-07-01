import gym
import gym_autonmscar
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines import DQN


env = gym.make('autonmscar-v0')
env = DummyVecEnv([lambda: env])

model = DQN(
    env=env,
    policy=MlpPolicy,
    verbose=1,
    tensorboard_log="./dqn_tensorboard/",
)

model.learn(total_timesteps=1000)

print("save the model")
model.save("test_model.pkl")
