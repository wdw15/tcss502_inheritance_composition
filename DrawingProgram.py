from DrawingProgramIterator import *

class DrawingProgram:
    def __init__(self, shape_list=None):
        if shape_list is None:
            shape_list = []

        self._shape_list = shape_list

    @property
    def shape_list(self):
        return self._shape_list

    @shape_list.setter
    def shape_list(self, shape_list):
        self._shape_list = shape_list

    def add_shape(self, shape):
        self._shape_list.append(shape)

    def remove_shape(self, shape):
        i=0
        for a_shape in self._shape_list:
            if a_shape.__name__.lower() == shape.lower():
                self._shape_list.remove(a_shape)
                i+=1
        return i

    def print_shape(self, shape_type):
        list_of_shapes = [shape_obj.draw() for shape_obj in self._shape_list if shape_type.lower() == shape_obj.__name__.lower()]
        return list_of_shapes

    def sort_shapes(self):
        self.__setup_merge__(list_of_shapes=self._shape_list, left=0, right=(len(self._shape_list) - 1))

    def get_shape(self, index):
        return self._shape_list[index]


    def set_shape(self, index, Shape):
        self._shape_list[index] = Shape

    def __iter__(self):
        return DrawingProgramIterator(self._shape_list)

    def __str__(self):
        string = ''
        for shape_str in self:
            string+=shape_str
            string+='\n'
        return string

    @staticmethod
    def __do_merge__(list_of_shapes, left, mid, right):
        """
        Args:
            list_of_shapes: array of Shape objects
            left: left most index
            mid: index of the end of left array
            right: index start of right array
        Returns: array of sorted clock objects
        """
        # Create empty arrays with _height of each side for number of cells to sort
        left_idx = 1+mid-left
        right_idx = right-mid
        left_array = [0]*left_idx
        right_array = [0]*right_idx

        # setup temp arrays with left value(s) and right value(s)
        for l in range(left_idx):
            left_array[l] = list_of_shapes[left + l]
        for r in range(right_idx):
            right_array[r] = list_of_shapes[mid + 1 + r]

        # re-initialize indexes, l for left and r for right to 0, initialize k for indexing list_of_shapes
        l = r = 0
        k = left

        # check arrays against one another and merge into list_of_shapes using the builtin methods __lt__ and __eq__
        while l < left_idx and r < right_idx:
            if left_array[l].__lt__(right_array[r]) or left_array[l].__eq__(right_array[r]):
                list_of_shapes[k] = left_array[l]
                l += 1
            # elif left_array[l].__eq__(right_array[r]):
            #     if left_array[l].__lt__(right_array[r]):
            #         list_of_shapes[k] = left_array[l]
            #     else:
            #         list_of_shapes[k] = right_array[r]
            else:
                list_of_shapes[k] = right_array[r]
                r += 1
            # index list_of_shapes for next position
            k += 1

        # still need to sort/assign left side if not finished
        while l < left_idx:
            list_of_shapes[k] = left_array[l]
            l += 1
            k += 1

        # still need to sort/assign right side if not finished
        while r < right_idx:
            list_of_shapes[k] = right_array[r]
            r += 1
            k += 1

    def __setup_merge__(self, list_of_shapes, left, right):
        """
        Args:
            list_of_shapes: array of Clock objects
            left: left most index, should start with 0
            right: right most index, should start with len(list_of_shapes)
        Returns: sorted clock objects in ascending order
        """
        if left < right:
            mid = (left + right) // 2

            self.__setup_merge__(list_of_shapes, left, mid)
            self.__setup_merge__(list_of_shapes, mid + 1, right)
            self.__do_merge__(list_of_shapes, left, mid, right)




