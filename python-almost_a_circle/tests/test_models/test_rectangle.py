#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_width(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 6
        self.assertEqual(r.width, 6)

        with self.assertRaises(ValueError):
            r.width = -1

        with self.assertRaises(TypeError):
            r.width = "not a number"

    def test_height(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.height = 7
        self.assertEqual(r.height, 7)

        with self.assertRaises(ValueError):
            r.height = -1

        with self.assertRaises(TypeError):
            r.height = "not a number"

    def test_x(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.x = 8
        self.assertEqual(r.x, 8)

        with self.assertRaises(ValueError):
            r.x = -1

        with self.assertRaises(TypeError):
            r.x = "not a number"

    def test_y(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.y = 9
        self.assertEqual(r.y, 9)

        with self.assertRaises(ValueError):
            r.y = -1

        with self.assertRaises(TypeError):
            r.y = "not a number"

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.display(), None)

    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(6, 8, 9, 7, 10)
        self.assertEqual(str(r), "[Rectangle] (6) 7/10 - 8/9")
        r.update(7, 5, 5, 5, 5)
        self.assertEqual(str(r), "[Rectangle] (7) 5/5 - 5/5")

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        d = r.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})


if __name__ == '__main__':
    unittest.main()
