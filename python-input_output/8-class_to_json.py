#!/usr/bin/python3
"""
function that returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """ Return a dictionary representation
    of an object for JSON serialization """
    return obj.__dict__
