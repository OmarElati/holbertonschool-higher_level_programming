#!/usr/bin/python3
"""
This is a class for representing a square.
"""


class Square:
    """
    Define a square with a private size attribute and public area method.
    """
    def __init__(self, size=0):
        """
        Initialize a square with optional size attribute.
        Raise TypeError if size is not an integer.
        Raise ValueError if size is less than 0.

        :param size: int, optional size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size
