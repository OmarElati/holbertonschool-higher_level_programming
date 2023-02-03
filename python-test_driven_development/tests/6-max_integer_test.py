import unittest

def max_integer(list=[]):
    """
    Finds the max integer in a list of integers
    """
    if len(list) == 0:
        return None
    max_val = list[0]
    for i in list:
        if i > max_val:
            max_val = i
    return max_val

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_list_of_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_list_of_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_list_of_mixed_integers(self):
        self.assertEqual(max_integer([1, -2, 3, -4, 5]), 5)
        self.assertEqual(max_integer([-5, 4, -3, 2, -1]), 4)

if __name__ == '__main__':
    unittest.main()
