#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """ Load a json file from a filename """
    with open(filename, 'r') as file:
        """ Load a json file from a filename """
        return json.load(file)
