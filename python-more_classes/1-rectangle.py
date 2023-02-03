#!/usr/bin/python3
class Rectangle:
    def __init__(self, _Rectangle__width=0, _Rectangle__height=0):
        self._Rectangle__height = _Rectangle__height
        self._Rectangle__width = _Rectangle__width

    def set__Rectangle__width(self, _Rectangle__width):
        if _Rectangle__width is int :
            if _Rectangle__width < 0:
                raise ValueError('width must be >= 0')
            else :
                self._Rectangle__width = _Rectangle__width
        else :
            raise TypeError('width must be an integer')

    def set__Rectangle__height(self, _Rectangle__height):
        if _Rectangle__height is int :
            if _Rectangle__height < 0:
                raise ValueError('height must be >= 0')
            else :
                self._Rectangle__height = _Rectangle__height
        else :
            raise TypeError('height must be an integer')

    def _Rectangle__width(self):
        return self._Rectangle__width

    def _Rectangle__height(self):
        return self._Rectangle__height