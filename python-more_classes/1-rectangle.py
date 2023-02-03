#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.width
    @property
    def height(self):
        return self.height

    @width.setter
    def set_width(self, width):
        if width is int :
            if width < 0:
                raise ValueError('width must be >= 0')
            else :
                self.width = width
        else :
            raise TypeError('width must be an integer')

    @height.setter
    def set_height(self, height):
        if height is int :
            if height < 0:
                raise ValueError('height must be >= 0')
            else :
                self.height = height
        else :
            raise TypeError('height must be an integer')

    