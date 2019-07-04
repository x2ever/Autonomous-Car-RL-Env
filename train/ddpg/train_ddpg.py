import os
import numpy
import gym
import gym_autonmscar

from stable_baselines.ddpg.policies import LnMlpPolicy
from stable_baselines.bench import Monitor
from stable_baselines.results_plotter import load_results, ts2xy
from stable_baselines import DDPG
from stable_baselines.ddpg import AdaptiveParamNoiseSpec


TIMESTEPS = int(1e7) + 1

best_mean_reward = -numpy.inf
n_steps = 0
log_directory = os.path.dirname(os.path.realpath(__file__)) + "/ddpg-log/"
model_directory = os.path.dirname(os.path.realpath(__file__)) + "/ddpg-models/"


def callback(_locals, _globals):
    """
    Callback called at each step (for DQN an others) or after n steps (see ACER or PPO2)
    :param _locals: (dict)
    :param _globals: (dict)
    """
    global best_mean_reward, n_steps
    if (n_steps + 1) % 1000 == 0:
        x, y = ts2xy(load_results(log_directory), 'timesteps')
        if len(x) > 0:
            mean_reward = numpy.mean(y[-100:])
            print(x[-1], 'timesteps')
            print("Best mean reward: {:.2f} - Last mean reward per episode: {:.2f}".format(
                best_mean_reward, mean_reward))

        if mean_reward > best_mean_reward:
            best_mean_reward = mean_reward
            print("> Saving new best model")
            _locals['self'].save(
                model_directory + 'ddpg-model_' + str(n_steps + 1) + '.pkl')
    n_steps += 1
    return True


if __name__ == "__main__":
    os.makedirs(log_directory, exist_ok=True)
    os.makedirs(model_directory, exist_ok=True)

    env = gym.make('autonmscarContinuous-v0')
    env = Monitor(env, log_directory, allow_early_resets=True)

    param_noise = AdaptiveParamNoiseSpec(
        initial_stddev=0.1, desired_action_stddev=0.1)
    model = DDPG(
        env=env,
        policy=LnMlpPolicy,
        param_noise=param_noise,
        verbose=1,
        tensorboard_log="./ddpg_tensorboard/",
    )

    model.learn(
        total_timesteps=TIMESTEPS,
        callback=callback
    )
