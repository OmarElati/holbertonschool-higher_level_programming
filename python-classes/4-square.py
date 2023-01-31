#!/usr/bin/python3
"""
This is a class for representing a square.
"""


class Square:
    """
    Defines a square by:
        - size: private instance attribute
            - Property getter to retrieve it
            - Property setter to set it
              (size must be an integer and >= 0)
        - Instantiation with optional size
        - Method to return the current square area
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieve the size attribute"""
        return self._size

    @size.setter
    def size(self, value):
        """
        Set the size attribute
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Return the current square area"""
        return self.size ** 2
