#!/usr/bin/python3
"""
This module provides the Base class, which is the foundation
for all other classes in this project. The Base class manages
the ID attribute for all future classes and prevents duplication of code.
"""

import json


class Base:
    """ Base class for classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))
