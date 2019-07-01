# gym-autonmscar

Autonomous car simulation environment for RL agent.

## Usage

### Install

1. Clone this repository.

```shell
$ git clone https://github.com/Jueun-Park/gym-autonmscar.git
```

2. `cd` into `gym-autonmscar`, then install the requirements.

```shell
$ pip install -e .
```

You can use `virtualenv` for isolation of the training environment. The python version used in this project is python3.6.8.

### Train and load the model

Train the model using the test code. The test code used DQN implemented in the [`stable-baselines`](https://github.com/hill-a/stable-baselines).

```shell
$ python test/train_test.py
$ python test/load_test.py
```

You can check the graph using `tensorboard`.

```shell
$ tensorboard --logdir ./dqn_tensorboard/
```

## Details

### Observation space

The obs space is 363 dimensions.

* 360 dimension data of LiDAR, the range is 0 - 100.
  * Each value is the distance to obstacle every 0.5 degrees. The range of the angle is 0 to 180 degrees and the front of the car is 90 degrees.
* 2 dimension data of the position of the car, the range is the size of the map.
* A value of the speed of the car, the range is 1 - 10.

### Action space

The action space is 4 dimensions.

* up, down, left, right

### Rewards

1. When colliding the wall
    * `reward -= 10`
2. When getting the trophy
    * `reward += 100 / [seconds after start] + 1000`
3. Else status
    * `reward += [speed of the car]`

---

## References

* [Making a custom environment in gym](https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa)
* [`gym-worm`](https://github.com/kwk2696/gym-worm)
