import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = 0

    def show(self):
        print('x:' + str(self.x) + '\n' + 'y:' + str(self.y))

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, second_object_of_Point):
        self.distance = math.sqrt((self.x - second_object_of_Point.x)**2 + (self.y - second_object_of_Point.y)**2)
        print(self.distance)
