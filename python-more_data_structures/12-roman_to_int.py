#!/usr/bin/python3
roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    for i in range(len(roman_string)):
        x = roman_dict[roman_string[i]]
        y = roman_dict[roman_string[i-1]]
        if i > 0 and x > y:
            result += x - 2 * y
        else:
            result += roman_dict[roman_string[i]]
    return result
