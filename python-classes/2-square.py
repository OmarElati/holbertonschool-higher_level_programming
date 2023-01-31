#!/usr/bin/python3
"""
This is a class for representing a square.
"""
class Square:
    """Defines a square with a private attribute 'size'

    Args:
    size (int, optional): Size of the square. Defaults to 0.

    Raises:
    TypeError: If 'size' is not an integer.
    ValueError: If 'size' is less than 0.
    """
    def __init__(self, size=0):
        """Inits the square with an optional size

        Args:
        size (int, optional): Size of the square. Defaults to 0.

        Raises:
        TypeError: If 'size' is not an integer.
        ValueError: If 'size' is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
