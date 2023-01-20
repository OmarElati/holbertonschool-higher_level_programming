#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i != j and i < j) and i < 9:
            if (i == 8 and j == 9):
                print("{:d}{:d}".format(i, j))
            else:
                print("{:d}{:d}, ".format(i, j), end="")
