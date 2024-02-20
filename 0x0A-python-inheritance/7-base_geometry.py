#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """Represents base geometry"""
    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value

        Args:
            name (str): The name
            value (int): The value to be evaluated
         Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
