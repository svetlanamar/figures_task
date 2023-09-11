import unittest
from geometry.triangle import Triangle


class TestTriangle(unittest.TestCase):
    def test_calculate_area(self):
        triangle = Triangle(8,12,7)
        expected_area = 26.906086671978
        self.assertAlmostEqual(triangle.calculate_area(),expected_area, places=6)

    def test_is_right_shape(self):
        # Test the is_right_shape method of the Triangle class
        # Create a triangle with sides 3, 4, and 5 (a Pythagorean triple)
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_shape(), "It should be a right triangle.")

        # Create a triangle with sides 6, 8, and 10 (a scaled-up Pythagorean triple)
        triangle = Triangle(6, 8, 10)
        self.assertTrue(triangle.is_right_shape(), "It should be a right triangle.")

        # Create a triangle with sides 5, 6, and 7 (not a right triangle)
        triangle = Triangle(5, 6, 7)
        self.assertFalse(triangle.is_right_shape(), "It should not be a right triangle.")


if __name__ == "__main__":
    unittest.main()
