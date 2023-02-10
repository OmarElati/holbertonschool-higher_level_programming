#!/usr/bin/python3
"""
writes a string to a text file
"""


def write_file(filename="", text=""):
    """ write a file to stdout """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
