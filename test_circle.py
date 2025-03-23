## test_circle.py

import unittest
from circle import Circle  # Import the Circle class from circle.py

class TestCircleMethods(unittest.TestCase):

    def test_area(self):
        # Test area calculation for a circle with radius 5
        circle = Circle(5)
        self.assertEqual(circle.area(), 3.14 * 5 * 5)

    def test_perimeter(self):
        # Test perimeter calculation for a circle with radius 5
        circle = Circle(5)
        self.assertEqual(circle.perimeter(), 2 * 3.14 * 5)

if __name__ == "__main__":
    unittest.main()