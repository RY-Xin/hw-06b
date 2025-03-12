import unittest
from classify_triangle import classify_triangle

class TestTriangleClassification(unittest.TestCase):
    
    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral Triangle")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles Triangle")
        self.assertEqual(classify_triangle(5, 5, 7), "Isosceles Triangle")

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Triangle and Right")
        self.assertEqual(classify_triangle(7, 8, 9), "Scalene Triangle")

    def test_invalid(self):
        self.assertEqual(classify_triangle(1, 1, 2), "Invalid Triangle")
        self.assertEqual(classify_triangle(-3, 4, 5), "Invalid Triangle")
        self.assertEqual(classify_triangle(0, 4, 5), "Invalid Triangle")

if __name__ == '__main__':
    unittest.main()

