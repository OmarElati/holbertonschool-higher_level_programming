#!/usr/bin/python3
"""
Module for the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that represents a Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the Square instance"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
