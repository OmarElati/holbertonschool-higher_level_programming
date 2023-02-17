#!/usr/bin/python3
"""Unittest for base.py"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_id(self):
        """Test for id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(5)
        self.assertEqual(b2.id, 5)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(0)
        self.assertEqual(b4.id, 0)

    def test_to_json_string(self):
        """Test for to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        j = Base.to_json_string([d])
        self.assertTrue(type(j) is str)
        self.assertEqual(j, '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]')

    def test_from_json_string(self):
        """Test for from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        j = '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]'
        l = Base.from_json_string(j)
        self.assertTrue(type(l) is list)
        self.assertEqual(len(l), 1)
        self.assertTrue(type(l[0]) is dict)
        self.assertEqual(l[0], {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5})


if __name__ == '__main__':
    unittest.main()
