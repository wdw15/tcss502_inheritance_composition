from Shape import *

class Triangle(Shape):
    def __init__(self, side_a=None, side_b=None, side_c=None):
        super().__init__()
        if side_a is None:
            side_a = 1.0
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c
        self.__name__ = 'Triangle'

    @property
    def area(self):
        s = self._side_a+self._side_b+self._side_c / 2
        return (s*(s-self._side_a)*(s-self._side_b)*(s-self._side_c))**0.5

    @property
    def perimeter(self):
        return self._side_a + self._side_b + self._side_c


