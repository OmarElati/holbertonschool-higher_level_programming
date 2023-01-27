#!/usr/bin/python3
def print_list_integer(my_list=[], start=0, end=-1):
    if end == -1:
        end = len(my_list)
    for i in my_list[start:end]:
        print("{}".format(i))
