#!/usr/bin/python3
"""
Contains the inherits from function
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class
    that inherited from the specified class.

    args:
        obj: The object to check
        a_class: The class to be checked
    Returns:
        True if obj is an instance of a_class that inherited
        from the specified class
        Otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
