class Shape:
    def __init__(self, length):
        self.length = length
        self.shape_area = 0

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def area(self):
        self.shape_area = self.width * self.length
        print(self.shape_area)

