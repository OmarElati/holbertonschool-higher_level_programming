#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from unittest.mock import patch
from models.base import Base
from io import StringIO

class TestSquare(unittest.TestCase):
    """Tests for Square class"""

    def test_square_is_instance_of_rectangle(self):
        """Tests if Square is an instance of Rectangle"""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_square_inherits_from_base(self):
        """Tests if Square inherits from Base"""
        s = Square(5)
        self.assertIsInstance(s, Base)

    def test_square_attributes(self):
        """Tests if Square has size and position attributes"""
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 3)

    def test_square_str(self):
        """Tests __str__ method of Square"""
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), '[Square] (3) 1/2 - 5')

    def test_square_area(self):
        """Tests area method of Square"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_square_display(self):
        """Tests display method of Square"""
        s = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_square_update(self):
        """Tests update method of Square"""
        s = Square(5)
        s.update(4, 2, 3, 4)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_update_kwargs(self):
        """Tests update method of Square with **kwargs"""
        s = Square(5)
        s.update(size=2, x=3, y=4, id=5)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_to_dictionary(self):
        """Tests to_dictionary method of Square"""
        s = Square(5, 1, 2, 3)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 3, 'size': 5, 'x': 1, 'y': 2})

if __name__ == '__main__':
    unittest.main()
