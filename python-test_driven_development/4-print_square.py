#!/usr/bin/python3

def print_square(size):
    """
    Function that prints a square using '#'
    @size: size of the square
    """
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError('size must be an integer')

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if isinstance(size, float):
        size = int(size)
        for i in range(size):
            print('#' * size)
