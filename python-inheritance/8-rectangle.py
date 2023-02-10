#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """
    Defines a rectangle
    """
    def __init__(self, width, height):
        """
        checks and sets the default attributes of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
