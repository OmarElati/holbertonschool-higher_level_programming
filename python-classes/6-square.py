#!/usr/bin/python3
"""
Module for Square class.
"""


class Square:
    """
    Class that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new instance of the Square class.

        Args:
        - size (int): The size of the square .
        - position (tuple): The position of the square .
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
        - int: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
        - value (int): The new size of the square.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
        - tuple: The position of the square.
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
        - value (tuple): The new position of the square.

        Raises:
        - TypeError: If value is not a tuple of 2 positive integers.
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Get the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self._size ** 2

    def my_print(self):
        """
        Print the square.
        """
        for i in range(self._position[1]):
            print()
        for i in range(self._size):
            print(" " * self._position[0] + "#" * self._size)
        if self._size == 0:
            print()
