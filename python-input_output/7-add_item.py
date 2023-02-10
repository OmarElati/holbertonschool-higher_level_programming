#!/usr/bin/python3
"""
script that adds all arguments to a Python list
"""


import sys
import json


def save_to_json_file(my_obj, filename):
    """ Save an object to a file in JSON format """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """ Load an object from a file in JSON format """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except:
        return []


def add_items(filename, items):
    """ Add items to a list and save the list to a file in JSON format """
    my_list = load_from_json_file(filename)
    for item in items:
        my_list.append(item)
    save_to_json_file(my_list, filename)


filename = "add_item.json"
my_list = load_from_json_file(filename)
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, filename)
