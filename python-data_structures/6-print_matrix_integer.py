#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_string = ""
        for val in row:
            row_string += "{:d} ".format(val)
            print(row_string.strip())
