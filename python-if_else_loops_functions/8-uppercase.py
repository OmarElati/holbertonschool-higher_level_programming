#!/usr/bin/python3
def uppercase(string: str):
    for c in string:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print(chr(ord(c) - ord('a') + ord('A')), end="")
        else:
            print(c, end="")
    print("\n")
