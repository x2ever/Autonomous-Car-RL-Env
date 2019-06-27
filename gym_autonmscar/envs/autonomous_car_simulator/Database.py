class Database:
    def __init__(self, lidar, control, car):
        self.lidar = lidar
        self.control = control
        self.car = car
        self.stop = False
