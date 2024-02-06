#!/usr/bin/python3
"""Define a class Square with size val."""


class Square:
    """Represent a square with size val."""

    def __init__(self, size=0):
        """Initialize the class with size validation.

        Args:
            size (int): Size of the new square, defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
