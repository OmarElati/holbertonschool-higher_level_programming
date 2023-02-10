#!/usr/bin/python3
"""
reads a text file
"""


def read_file(filename=""):
    """ Read a file and return a string containing """
    with open(filename, 'r') as f:
        print(f.read(), end='')
