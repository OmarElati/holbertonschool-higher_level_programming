#!/usr/bin/python3
"""
function that writes an Object to a text file
"""


import json


def save_to_json_file(my_obj, filename):
    """ save to json file """
    with open(filename, 'w') as file:
        """ write to json file """
        json.dump(my_obj, file)
