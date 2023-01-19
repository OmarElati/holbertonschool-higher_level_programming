#!/usr/bin/python3
for i in range(97, 123):
    if i not in (101, 113):
        x = chr(i)
        print(x.format(chr(i)), end='')
