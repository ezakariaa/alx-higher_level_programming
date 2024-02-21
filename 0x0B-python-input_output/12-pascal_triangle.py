#!/usr/bin/python3
"""Defines a Pascal Triangle function."""


def pascal_triangle(n):
    """Represents Pascal Triangle of size n.
    returns a list of lists of integer.
    """
    if n <= 0:
        return []

    list_tri = [[1]]
    while len(list_tri) != n:
        triangle = list_tri[-1]
        t = [1]
        for i in range(len(triangle) - 1):
            t.append(triangle[i] + triangle[i + 1])
        t.append(1)
        list_tri.append(t)
    return list_tri
