#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(10, 20, 0, 0, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(5, 5)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertIsNotNone(r2.id)

    def test_getters_setters(self):
        r = Rectangle(10, 20, 0, 0, 1)

        r.width = 5
        self.assertEqual(r.width, 5)

        r.height = 10
        self.assertEqual(r.height, 10)

        r.x = 1
        self.assertEqual(r.x, 1)

        r.y = 2
        self.assertEqual(r.y, 2)

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

        r.width = 5
        r.height = 5
        self.assertEqual(r.area(), 25)

    def test_display(self):
        r = Rectangle(2, 3)

        expected_output = "##\n" * 3
        self.assertEqual(r.display(), expected_output)

        expected_output = "  ##\n  ##\n  ##\n"
        self.assertEqual(r.display(x=2, y=1), expected_output)

if __name__ == '__main__':
    unittest.main()
