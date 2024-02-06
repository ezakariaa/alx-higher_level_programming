#!/usr/bin/python3
"""Define a MagicClass that matches a specific bytecode."""

import math


class MagicClass:
    """Represent a circle with methods for area and circumference."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (number): The radius of the circle.

        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
