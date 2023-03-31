#!/usr/bin/python3
""" This module contains functions that can be used to create rectangles """


class Rectangle:
    """A class that defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the Rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """
        Return a string representation of
        the Rectangle for use with eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when a Rectangle instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
