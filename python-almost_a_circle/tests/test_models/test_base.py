#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_autoincrement(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_manual(self):
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

    def test_id_invalid_type(self):
        with self.assertRaises(TypeError):
            b1 = Base("string")
