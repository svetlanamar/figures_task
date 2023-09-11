from geometry.shapes import Shape
import math


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def is_right_shape(self):
        # not applicable here
        pass
