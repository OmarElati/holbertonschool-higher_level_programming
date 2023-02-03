===================================================
Tests for matrix_divided in 2-matrix_divided.py
===================================================

>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

>>> matrix_divided([[1, 2, 3],[4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

>>> matrix_divided([[1, 2, 3],[4, 5, 6]], 2)
[[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

>>> matrix_divided([[1, 2, 3],[4, 5, 6],[7, 8, 9]], 2)
[[0.5, 1.0, 1.5], [2.0, 2.5, 3.0], [3.5, 4.0, 4.5]]

>>> matrix_divided([[1, 2, 3],[4, 5, 6]], 0)
Traceback (most recent call last):
...
ZeroDivisionError: division by zero

>>> matrix_divided("Hello", 5)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix_divided([[1, 2, 3],[4, 5, 6]], "Hello")
Traceback (most recent call last):
...
TypeError: div must be a number

>>> matrix_divided([[1, 2, 3],[4, 5]], 2)
Traceback (most recent call last):
TypeError: Each row of the matrix must have the same size

>>> matrix_divided((1, 2), 2)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix_divided([[2,3],[3, 4]])
Traceback (most recent call last):
TypeError: matrix_divided() missing 1 required positional argument: 'div'

>>> matrix_divided([[3, "a"], [12, 3]], 3)
Traceback (most recent call last):
TypeError: unsupported operand type(s) for /: 'str' and 'int'
