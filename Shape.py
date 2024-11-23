from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name=None):
        if name is None:
            name = 'None'
        self.__name__ = name

    @property
    def name(self):
        return self.__name__

    @name.setter
    def name(self, name):
        self.__name__ = name

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def draw(self):
        """ name_of_shape, area: value_of_area, perimeter: value_of_perimeter
        ex. Circle, area: 3.141592653589793, perimeter: 6.283185307179586 """
        return self.__str__()

    def __str__(self):
        return f'{self.__name__}, area: {self.area}, perimeter: {self.perimeter}'

    def __lt__(self, Shape):
        if self.__name__.lower() < Shape.__name__.lower():
            return True
        elif self.__name__.lower() > Shape.__name__.lower():
            return False
        else:
            return self.area < Shape.area

    def __gt__(self, Shape):
        if self.__name__.lower() > Shape.__name__.lower():
            return True
        elif self.__name__.lower() < Shape.__name__.lower():
            return False
        else:
            return self.area > Shape.area

    def __eq__(self, Shape):
        return self.area == Shape.area and self.__name__.lower() == Shape.__name__.lower()



