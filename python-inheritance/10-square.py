#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""


Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """ class instantiation """
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ method that returns the area of the square """
        return self.__size ** 2
