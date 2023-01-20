#!/usr/bin/python3
def uppercase(string: str):
    result = ""
    for c in string:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            result += chr(ord(c) - ord('a') + ord('A'))
        else:
            result += c
    print(result)
    print("\n")
