#!/usr/bin/python3
def uppercase(string: str):
    result = ""
    for c in string:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            result += chr(ord(c) - ord('a') + ord('A'))
        else:
            result += c
    print('{0}'.format(result))
    print("\n")
