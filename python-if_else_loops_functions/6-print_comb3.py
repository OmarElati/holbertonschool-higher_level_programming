#!/usr/bin/python3
for i in range(10):
    if (i == 8 and j == 9):
        print("{:d}{:d}".format(i, j))
    for j in range(i+1,10):
        print("{:d}{:d}, ".format(i, j), end="")
