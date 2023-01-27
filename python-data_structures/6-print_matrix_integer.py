#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (len(matrix) == 1 and any(matrix) is False):
        print()
    for row in matrix:
        count = 0
        for n in row:
            if count == len(row) - 1:
                print("{:d}".format(n), end="")
                print()
            else:
                print("{}".format(n), end="")
            count += 1
