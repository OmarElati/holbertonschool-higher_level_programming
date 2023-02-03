#!/usr/bin/python3
"""
    Since the beginning you have been creating “Interactive tests”.
    For this exercise, you will add Unittests.
"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
        class for cases
    """

    def test_cases(self):
        """
            test cases for function
        """
        self.assertEqual(max_integer([13, 0, 56, 3]), 56)
        self.assertEqual(max_integer([-3, -6, -1, -67]), -1)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-5, 0, 6]), 6)
        self.assertEqual(max_integer([73210584, 58, -68, 3]), 73210584)
        self.assertEqual(max_integer([1, 6]), 6)
        self.assertEqual(max_integer([87]), 87)
        self.assertEqual(max_integer([6, 8, 10e1000]), float('inf'))
        self.assertEqual(max_integer([87, float('nan'), 5]), 87)
        self.assertEqual(max_integer("Holberton"), 't')

if __name__ == '__main__':
    unittest.main()
