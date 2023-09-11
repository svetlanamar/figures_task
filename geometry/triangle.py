from geometry.shapes import Shape
import math


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    ''' Area = √[s(s-a)(s-b)(s-c)]
    Here, "s" is the semi-perimeter of the triangle, i.e., s = (a + b + c)/2. '''

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    def is_right_shape(self):
        sides = [self.a, self.b, self.c]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
