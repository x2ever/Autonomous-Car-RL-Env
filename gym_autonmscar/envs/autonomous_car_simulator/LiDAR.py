import inspect
import sys
import platform
import numpy as np

from Authority import AuthorityExecption


class LiDAR:
    def __init__(self):
        self.__data = np.zeros((360))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        if platform.system() == 'Windows':
            if inspect.stack()[1][1].split('\\')[-1] == 'Game.py':
                self.__data = new_data
            else:
                sys.tracebacklimit = 0
                raise AuthorityExecption('Not allowed File %s is trying to change LiDAR.data at \'%s\'' % (
                    inspect.stack()[1][1].split('\\')[-1], inspect.stack()[1][0]))
        else:
            if inspect.stack()[1][1].split('/')[-1] == 'Game.py':
                self.__data = new_data
            else:
                sys.tracebacklimit = 0
                raise AuthorityExecption('Not allowed File %s is trying to change LiDAR.data at \'%s\'' % (
                    inspect.stack()[1][1].split('/')[-1], inspect.stack()[1][0]))
