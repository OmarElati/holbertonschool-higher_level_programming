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
            return {key: value for key, value in self.__dict__.items()}
        else:
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
                }

    def reload_from_json(self, json):
        """ Reload from a JSON representation """
        for key, value in json.items():
            setattr(self, key, value)
