#!/usr/bin/python3
"""
    class MyList that inherits from list
"""


class MyList(list):
    """ MyList class """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(self))
