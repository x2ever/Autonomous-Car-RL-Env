import inspect

class LiDAR:
    def __init__(self):
        self.__data = None
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        if inspect.stack()[1][1].split('\\')[-1] == "Game.py":
            # Check if this code is working, on Linux
            self.__data = new_data