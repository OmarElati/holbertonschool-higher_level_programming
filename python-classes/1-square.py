#!/usr/bin/python3
class Square:
    """
    Defines a square with a private instance attribute size.
    Instantiation with size (no type/value verification).
    """
    def __init__(self, size=0):
        """
        Initialize a square object with a given size.
        :param size: size of the square (default is 0)
        """
        self.__size = size
