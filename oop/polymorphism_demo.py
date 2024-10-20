import math
from math import radians


class Shape:
    def area(self):
        raise NotImplementedError("derived classes need to override this method")

class Rectangle(Shape):
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius*self.radius)