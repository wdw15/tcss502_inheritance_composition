

class DrawingProgramIterator:
    def __init__(self, shape_list):
        self._shape_list = shape_list
        self.index = 0

    def __next__(self):
        if self.index == len(self._shape_list):
            raise StopIteration()

        shape = self._shape_list[self.index]
        self.index += 1
        return shape.draw()

    def __iter__(self):
        return self







