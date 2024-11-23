from circle import Circle
from square import Square
from triangle import Triangle
from rectangle import Rectangle

class ShapeFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_circle(radius=None):
        return Circle(radius)

    @staticmethod
    def create_square(length=None):
        return Square(length)

    @staticmethod
    def create_triangle(side_a=None, side_b=None, side_c=None):
        return Triangle(side_a, side_b, side_c)

    @staticmethod
    def create_rectangle(width=None, height=None):
        return Rectangle(width, height)





