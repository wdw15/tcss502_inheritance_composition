from Shape import *
import numpy as np

class Circle(Shape):
    def __init__(self, radius=None):
        super().__init__()
        if radius is None:
            radius = 1.0
        self._radius = radius
        self.__name__ = 'Circle'

    @property
    def area(self):
        return self._radius * self._radius * np.pi

    @property
    def perimeter(self):
        return 2 * self._radius * np.pi


