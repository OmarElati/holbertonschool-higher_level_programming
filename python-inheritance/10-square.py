#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""


class BaseGeometry:
    """
    Defines the BaseGeometry class.
    """
    def area(self):
        """
        raises an Exception with the message
        area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates an intger value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Defines a rectangle with private height and width
    """
    def __init__(self, width, height):
        """ Initial value"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ returns the string representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
