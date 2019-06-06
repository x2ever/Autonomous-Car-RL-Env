## Autonomous Car Simulator

This code will be used at Hackathon hosted by the autonomous driving club ThinKingo.

### 2019 ThinKingo Autonomous Car Hackathon


__Date__ : 2019-06-07 ~ 2019-06-08

__Participants__: Sungkyunkwan University individual or team

__Preliminary team composition__: Maximum 4 people per team (individual participants are assigned by the organizer)

__Instructions__:
- Free breakfast and dinner
- Award for Top 3 teams

__Summary of Competition__: Implementation of path generation and obstacle avoidance algorithm using virtual LiDAR data provided in simulator

__Jury Introduction__:

Jiwoo Jeong
- CEO of [Gepetto Robotics](https://www.gepetto.io/)
- SKKU Master of Mechanical Engineering

__Competition schedule__:

```
FRI
18:30 ~ 18:45 Meeting organizer introduction time
18:45 ~ 19:30 Dinner and social hour
19:30 ~ 20:30 Pre-training seminar
20:30 ~       Start Hackathon

SAT
07:00 ~ 08:00 Breakfast
      ~ 08:30 Submission of results
09:00 ~ 09:30 Product demonstration and evaluation
09:30 ~ 10:00 Time of awards ceremony
```

### Preview

#### LiDAR

Participants receive virtual LiDAR and GPS data.

![LiDAR_preview.png](https://github.com/x2ever/HEVEN-AutonomousCar-2019/blob/master/ThinKingo-Hackathon/images/LiDAR_preview.png)

#### Course

If the participants complete the route in the shortest time, they will win.

![level1](https://github.com/x2ever/HEVEN-AutonomousCar-2019/blob/master/ThinKingo-Hackathon/images/level1.png)


### Usage

#### Auto

Drive with your own algorithm which is implemented at `Brain.py`.
```
python main.py --auto
```

#### Not auto

Drive with Keyboard.

```
python main.py
```
