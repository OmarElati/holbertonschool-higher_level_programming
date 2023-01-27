#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            integers_printed += 1
        except(ValueError, TypeError):
            break
    print()
    return integers_printed
