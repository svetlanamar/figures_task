from geometry.circle import Circle
from geometry.triangle import Triangle

my_circle = Circle(23)
circle_area = my_circle.calculate_area()

print(f"The area of the circle is {circle_area}.")

# calculating the triangle
a = 8
b = 12
c = 7

my_triangle = Triangle(a, b, c)

area = my_triangle.calculate_area()
is_right = my_triangle.is_right_shape()

print("Area of the triangle:", area)
print("Is it a right triangle?", is_right)

