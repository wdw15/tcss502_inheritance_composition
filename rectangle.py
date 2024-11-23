from Shape import *

class Rectangle(Shape):
    def __init__(self, width=None, height=None,):
        super().__init__()
        if width is None:
            width = 1.0
        if height is None:
            height = 1.0
        self._width = width
        self._height = height
        self.__name__ = 'Rectangle'

    @property
    def area(self):
        return self._height * self._width

    @property
    def perimeter(self):
        return (2 * self._height) + (2 * self._width)



