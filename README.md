## Autonomous Car Simulator

This code will be used at Hackathon hosted by the autonomous driving club ThinKingo.

### 2019 ThinKingo Autonomous Car Hackathon


__Date__ : 2019-06-07 ~ 2019-06-08

__Participants__: Sungkyunkwan University individual or team

__Preliminary team composition__: Maximum 4 people per team (individual participants are assigned by the organizer)

__Instructions__:
- Free breakfast and dinner
- Award for Top 4 teams

__Summary of Competition__: Implementation of path generation and obstacle avoidance algorithm using virtual LiDAR data provided in simulator

__Competition schedule__:

```
금
17:30 ~ 18:00 Meeting organizer introduction time
18:00 ~ 19:00 Dinner and social hour
19:00 ~ 20:00 Pre-training seminar
20:00 ~       Start Hackathon

토
07:00 ~ 08:00 Breakfast
      ~ 08:30 Submission of results
09:00 ~ 09:30 Product demonstration and evaluation
09:30 ~ 10:00 ime of awards ceremony
```

### Preview

#### LiDAR

Participants receive virtual LiDAR and GPS data.

![LiDAR_preview.png](/images/LiDAR_preview.png)

#### Course

If the participants complete the route in the shortest time, they will win.

![level1](/images/level1.png)


### Usage

#### Auto

Drive with Keyboard
```
python main.py --auto
```

#### Not auto

Drive with your own algorithm which is implemented at `Brain.py`.

```
python main.py
```
