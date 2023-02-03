#!/usr/bin/python3
"""
..
"""


class Rectangle:
    """
    ..
    """
    def __init__(self, width=0, height=0):
        """.."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """.."""
        return self.width

    @property
    def height(self):
        """.."""
        return self.height

    @width.setter
    def width(self, value):
        """.."""
        if isinstance(value, int):

            if value >= 0:
                self.__width = value
            else:
                raise ValueError('width must be >= 0')

        else:
            raise TypeError('width must be an integer')

    @height.setter
    def height(self, value):
        """.."""
        if isinstance(value, int):

            if value >= 0:
                self.__width = value
            else:
                raise ValueError('height must be >= 0')

        else:
            raise TypeError('height must be an integer')
