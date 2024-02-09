"""Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have an area function which can print the area of the shape where Shape's area is 0 by default."""

"""In this case we have to add to parent class with __init__ and variables to it, because in other way it has no sense to make child class for it!!!"""


class Shape:
    """SuperClass"""
    def __init__(self, length, width=0):
        self.length = length
        self.width = width
        self.shape_area = 0

    def area(self):
        if self.width != 0:
            self.shape_area = self.length * self.width
            print(self.shape_area)
        if self.width == 0:
            print('Area is zero')


class Square(Shape):
    """SubClass"""
    def __init__(self, length):
        super().__init__(length)
        self.shape_area = 0

    def area(self):
        self.shape_area = self.length * self.length
        print(self.shape_area)




