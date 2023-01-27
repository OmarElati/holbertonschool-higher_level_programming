#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if type(my_list_1[i]) not in (int, float) or type(my_list_2[i]) not in (int, float):
                print("wrong type")
                new_list.append(0)
            elif my_list_2[i] == 0:
                print("division by 0")
                new_list.append(0)
            else:
                new_list.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            new_list.append(0)
    return new_list

