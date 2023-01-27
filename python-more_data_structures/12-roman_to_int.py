#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    prev_val = 0
    for char in roman_string[::-1]:
        if roman_map[char] >= prev_val:
            int_val += roman_map[char]
        else:
            int_val -= roman_map[char]
            prev_val = roman_map[char]
        return int_val
