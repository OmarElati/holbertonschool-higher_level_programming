import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_attributes(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

    def test_setters(self):
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

        with self.assertRaises(TypeError):
            s1.size = "hello"
        with self.assertRaises(ValueError):
            s1.size = -1

    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_display(self):
        s1 = Square(3)
        output = s1.display()
        self.assertIsNone(output)

    def test_str(self):
        s1 = Square(4, 2, 3, 99)
        self.assertEqual(str(s1), "[Square] (99) 2/3 - 4")
        
    def test_update(self):
        s1 = Square(5)
        s1.update(6, 7, 8, 9)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)

        s1.update(size=10, y=4, x=3, id=5)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        
if __name__ == '__main__':
    unittest.main()
