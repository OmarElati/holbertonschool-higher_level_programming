#!/usr/bin/python3
"""
    adds 2 integers
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
    a (int or float): The first integer to be added.
    b (int or float, optional): The second integer to be added. Defaults to 98.

    Raises:
    TypeError: If a or b is not an integer or float.
    The error message will be "a must be an integer" or "b must be an integer".

    Returns:
    int: The sum of the two integers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
