import gym
import gym_autonmscar

env = gym.make('autonmscar-v0')

for i in range(3):
    obs = env.reset()
    for t in range(1000):
        env.render()
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

env.close()
