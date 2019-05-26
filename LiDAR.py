class LiDAR:
    def __init__(self):
        self.__data = None
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data