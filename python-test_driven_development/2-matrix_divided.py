#!/usr/bin/python3
"""
This module contains the matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix. Returns a
    new matrix (list of list). The result is
    rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) is 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

    for i in row:
        if type(i) != int and type(i) != float:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elements == len_rows[0] for elements in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    NEW_matrix = [[round(i / div, 2) for i in row] for row in matrix]
    return NEW_matrix
