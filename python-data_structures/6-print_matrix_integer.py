#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i,val in enumerate(row):
            print("{:d}".format(val), end=" ")
        print()
