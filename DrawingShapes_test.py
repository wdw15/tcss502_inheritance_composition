import unittest
from DrawingProgram import *
from ShapeFactory import *
import numpy as np

class DrawingProgramTests(unittest.TestCase):

    def test_shape_factory(self):
        circle = ShapeFactory.create_circle(2.0)
        rect = ShapeFactory.create_rectangle(3, 9)
        square = ShapeFactory.create_square(7)
        triangle = ShapeFactory.create_triangle(10, 20, 30)

        self.assertEqual(isinstance(circle, Circle), True)
        self.assertEqual(isinstance(rect, Rectangle), True)
        self.assertEqual(isinstance(square, Square), True)
        self.assertEqual(isinstance(triangle, Triangle), True)


    def test_shape_area(self):
        circle = ShapeFactory.create_circle(2.0)
        rect = ShapeFactory.create_rectangle(3, 9)
        square = ShapeFactory.create_square(7)
        triangle = ShapeFactory.create_triangle(10, 20, 30)

        self.assertEqual(circle.area, np.pi*2**2)
        self.assertEqual(rect.area, 3*9)
        self.assertEqual(square.area, 7**2)

        s = 10+20+30 / 2
        tri_area = (s*(s-10)*(s-20)*(s-30))**0.5
        self.assertEqual(triangle.area, tri_area)


    def test_shape_perimeter(self):
        circle = ShapeFactory.create_circle(2.0)
        rect = ShapeFactory.create_rectangle(3, 9)
        square = ShapeFactory.create_square(7)
        triangle = ShapeFactory.create_triangle(10, 20, 30)

        self.assertEqual(circle.perimeter, np.pi*2*2)
        self.assertEqual(rect.perimeter, 3*2 + 9*2)
        self.assertEqual(square.perimeter, 7*4)
        self.assertEqual(triangle.perimeter, 60)


    def test_get_name(self):
        circle = ShapeFactory.create_circle(6.0)
        rect = ShapeFactory.create_rectangle(7, 2)
        square = ShapeFactory.create_square(4)
        triangle = ShapeFactory.create_triangle(2, 4, 6)

        self.assertEqual(circle.name.lower(), 'circle')
        self.assertEqual(rect.name.lower(), 'rectangle')
        self.assertEqual(square.name.lower(), 'square')
        self.assertEqual(triangle.name.lower(), 'triangle')


    def test_check_print(self):
        circle = ShapeFactory.create_circle(2.0)
        tri = ShapeFactory.create_triangle(1,2,3)
        rect = ShapeFactory.create_rectangle(3, 9)
        square = ShapeFactory.create_square(7)
        drawing_prog = DrawingProgram([circle,tri,rect,square])

        self.assertEqual(drawing_prog.print_shape('triangle')[0], tri.draw())
        self.assertEqual(drawing_prog.print_shape('square')[0], square.draw())
        self.assertEqual(drawing_prog.print_shape('rectangle')[0], rect.draw())
        self.assertEqual(drawing_prog.print_shape('circle')[0], circle.draw())


    def test_sort_shapes(self):
        circle1 = ShapeFactory.create_circle(1.0)
        circle2 = ShapeFactory.create_circle(2.0)
        tri1 = ShapeFactory.create_triangle(1,2,3)
        tri2 = ShapeFactory.create_triangle(4,5,6)
        rect1 = ShapeFactory.create_rectangle(3, 6)
        rect2 = ShapeFactory.create_rectangle(9, 9)
        rect3 = ShapeFactory.create_rectangle(1, 2)
        square = ShapeFactory.create_square(7)

        drawing_prog = DrawingProgram([circle1,circle2,tri1,tri2,rect1,rect2,rect3,square])
        drawing_prog.sort_shapes()
        self.assertEqual(drawing_prog.get_shape(0), circle1)
        self.assertEqual(drawing_prog.get_shape(-1), tri2)
        self.assertEqual(drawing_prog.get_shape(3), rect1)


    def test_iterator_nominal(self):
        circle = ShapeFactory.create_circle(2.0)
        tri = ShapeFactory.create_triangle(1,2,3)
        rect = ShapeFactory.create_rectangle(3, 9)
        square = ShapeFactory.create_square(7)

        drawing_prog = DrawingProgram([circle,tri,rect,square])

        for shape in drawing_prog:
            print(shape)
            self.assertEqual(isinstance(shape, str), True)


    def test_iterator_one(self):
        tri = ShapeFactory.create_triangle(10,45,90)
        drawing_prog = DrawingProgram([tri])

        for shape in drawing_prog:
            print(shape)
            self.assertEqual(isinstance(shape, str), True)


    def test_iterator_zero(self):
        drawing_prog = DrawingProgram()

        for shape in drawing_prog:
            print(shape)
            self.assertEqual(isinstance(shape, str), True)


    def test_set_shape(self):
        circle = ShapeFactory.create_circle(2.0)
        tri = ShapeFactory.create_triangle(1,2,3)
        rect = ShapeFactory.create_rectangle(3, 9)

        drawing_prog = DrawingProgram([circle,tri,rect])

        square = ShapeFactory.create_square(7)

        drawing_prog.set_shape(0, square)
        self.assertEqual(drawing_prog.get_shape(0), square)

        drawing_prog.set_shape(2, circle)
        self.assertEqual(drawing_prog.get_shape(2), circle)


    def test_remove_shape(self):
        circle = ShapeFactory.create_circle(2.0)
        tri = ShapeFactory.create_triangle(1,2,3)
        rect = ShapeFactory.create_rectangle(4, 2)
        square = ShapeFactory.create_square(9)

        drawing_prog = DrawingProgram([circle,tri,rect,square])

        self.assertEqual(drawing_prog.remove_shape('circle'), 1)
        self.assertNotEqual(drawing_prog.get_shape(0), circle)


    def test_drawingprog_str_(self):
        circle = ShapeFactory.create_circle(7.0)
        tri = ShapeFactory.create_triangle(9,8,7)
        rect = ShapeFactory.create_rectangle(56, 87)
        square = ShapeFactory.create_square(100)

        drawing_prog = DrawingProgram([circle,tri,rect,square])

        test_string = (f'{circle.draw()}\n'
                       f'{tri.draw()}\n'
                       f'{rect.draw()}\n'
                       f'{square.draw()}\n')

        self.assertEqual(drawing_prog.__str__(), test_string)
















