 #!/usr/bin/python3
"""Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(10, 2, 1, 1, 12)

    def test_id_value(self):
        self.assertEqual(self.r2.id, 12)

    def test_width_value(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 10)

    def test_height_value(self):
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 2)
    
    def test_x_value(self):
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 1)
    
    def test_y_value(self):
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 1)

    def test_area(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 20)

    def test_str(self):
        self.assertEqual(str(self.r2), "[Rectangle] (12) 1/1 - 10/2")

if __name__ == '__main__':
    unittest.main()
