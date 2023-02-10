#!/usr/bin/python3
"""
class Student
"""


class Student:
    """ defines a student """
    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return a JSON representation """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {
                attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)
            }
