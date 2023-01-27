#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        new_list.append(i % 2 == 0)
    return new_list
