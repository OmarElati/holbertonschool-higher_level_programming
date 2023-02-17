#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from models.base import Base
from models.square import Square
import io

class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle"""

    def test_rectangle_width(self):
        """Test width of the Rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

    def test_rectangle_height(self):
        """Test height of the Rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)

    def test_rectangle_x(self):
        """Test x attribute of the Rectangle"""
        r1 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r1.x, 3)

    def test_rectangle_y(self):
        """Test y attribute of the Rectangle"""
        r1 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r1.y, 4)

    def test_rectangle_id(self):
        """Test id attribute of the Rectangle"""
        r1 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r1.id, 5)

    def test_rectangle_area(self):
        """Test area method of the Rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

    def test_rectangle_init_string(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_rect_str_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")


    def test_rectangle_display(self):
        """Test display method of the Rectangle"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.display(), print("###\n###\n"))

    def test_rectangle_str(self):
        """Test __str__ method of the Rectangle"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_update(self):
        """Test update method of the Rectangle"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_rectangle_update_args_kwargs(self):
        """Test update method with *args and **kwargs of the Rectangle"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5, id=98, width=99, height=100, x=101, y=102)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_rectangle_to_dictionary(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        r1_dict = r1.to_dictionary()
        r1_dict_expected = {'id': 12, 'width': 10, 'height': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(r1_dict, r1_dict_expected)

        r2 = Rectangle(1, 1, 1, 1, 1)
        r2_dict = r2.to_dictionary()
        r2_dict_expected = {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        self.assertDictEqual(r2_dict, r2_dict_expected)

        r3 = Rectangle(10, 5, 2, 7, 2)
        r3_dict = r3.to_dictionary()
        r3_dict_expected = {'id': 2, 'width': 10, 'height': 5, 'x': 2, 'y': 7}
        self.assertDictEqual(r3_dict, r3_dict_expected)


    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_display(self):
        r = Rectangle(2, 3)
        expected_output = "##\n" * 3
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            r.display()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (89) 2/5 - 1/1")
        r.update(y=1, width=2, x=3, id=98)
        self.assertEqual(str(r), "[Rectangle] (98) 3/1 - 2/1")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 14)
        expected_output = {'x': 1, 'y': 9, 'id': 14, 'width': 10, 'height': 2}
        self.assertDictEqual(r.to_dictionary(), expected_output)
