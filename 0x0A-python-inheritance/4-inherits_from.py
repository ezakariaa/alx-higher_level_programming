#!/usr/bin/python3
"""
Contains the inherits from function
"""


def inherits_from(obj, a_class):
    """returns True if object is a subclass of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
