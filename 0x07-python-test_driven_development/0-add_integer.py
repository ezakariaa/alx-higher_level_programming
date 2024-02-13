#!/usr/bin/python3

"""Defines two integer addition function."""


def add_integer(a, b=98):
    """adds two integers & returns the addition.

    args:
    a (int or float): First number to be added
    b (int or float): Second number to be added

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
