#!/usr/bin/python3
"""Unittest for base.py"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for base.py"""

    def test_assign_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_id_increment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_base_init_with_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)
        b2 = Base(90)
        self.assertEqual(b2.id, 90)
        b3 = Base()
        self.assertEqual(b3.id, 1)

    def test_to_json_string_with_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_constructor(self):
        """Test Base constructor"""
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(12)
        self.assertEqual(b.id, 12)
        b = Base(-4)
        self.assertEqual(b.id, -4)

    def test_to_json_string(self):
        """Test Base to_json_string method"""
        list_dicts = [{'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5},
                      {'id': 6, 'x': 7, 'y': 8, 'width': 9, 'height': 10}]
        json_str = Base.to_json_string(list_dicts)
        expected = '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}, \
{"id": 6, "x": 7, "y": 8, "width": 9, "height": 10}]'
        self.assertEqual(json_str, expected)

        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, '[]')

    def test_from_json_string(self):
        """Test Base from_json_string method"""
        json_str = '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}, \
{"id": 6, "x": 7, "y": 8, "width": 9, "height": 10}]'
        expected = [{'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5},
                    {'id': 6, 'x': 7, 'y': 8, 'width': 9, 'height': 10}]
        list_dicts = Base.from_json_string(json_str)
        self.assertEqual(list_dicts, expected)

        list_dicts = Base.from_json_string(None)
        self.assertEqual(list_dicts, [])

    def test_save_to_file(self):
        """Test Base save_to_file method"""
        b1 = Base()
        b2 = Base()
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as f:
            file_content = f.read()
            self.assertEqual(file_content, '[{}, {}]')

        b3 = Base(10)
        b4 = Base(11)
        Base.save_to_file([b1, b2, b3, b4])
        with open("Base.json", "r") as f:
            file_content = f.read()
            expected = '[{"id": 1}, {"id": 2}, {"id": 10}, {"id": 11}]'
            self.assertEqual(file_content, expected)

if __name__ == '__main__':
    unittest.main()
