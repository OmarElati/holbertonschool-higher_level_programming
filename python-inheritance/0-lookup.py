#!/usr/bin/python3
"""
Lookup all attributes of an object
"""


def lookup(obj):
    """
    function that returns the list of available attributes
    """
    result = []
    for attr in dir(obj):
        result.append(attr)
    return result
