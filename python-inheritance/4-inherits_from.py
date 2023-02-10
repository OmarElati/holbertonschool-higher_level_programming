#!/usr/bin/python3
"""
function that compares the object is exactly an instance.
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from
    the specified class ; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
