import unittest
from geometry.circle import Circle


class TestCircle(unittest.TestCase):
    def test_calculate_area(self):
        circle = Circle(23)
        expected_area = 1661.9025137490005
        self.assertAlmostEqual(circle.calculate_area(), expected_area, places=6)


if __name__ == "__main__":
    unittest.main()
