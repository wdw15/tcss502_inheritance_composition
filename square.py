from Shape import *

class Square(Shape):
    def __init__(self, length=None):
        super().__init__()
        if length is None:
            length = 1.0
        self._length = length
        self.__name__ = 'Square'

    @property
    def area(self):
        return self._length**2

    @property
    def perimeter(self):
        return 4 * self._length



