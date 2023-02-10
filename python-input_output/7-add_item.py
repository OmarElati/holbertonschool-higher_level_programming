#!/usr/bin/python3
"""

"""


import sys
import json


def save_to_json_file(my_obj, filename):
    """ save to json file """
    with open(filename, 'w') as file:
        """ save to json file """
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """ load from json file """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except:
        return []

filename = "add_item.json"
my_list = load_from_json_file(filename)
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, filename)
