#!/usr/bin/python3
def no_c(my_string):
    res = []
    for x in my_string:
        if x != 'c' and x != 'C':
            res.append(x)
    return ("".join(res))
