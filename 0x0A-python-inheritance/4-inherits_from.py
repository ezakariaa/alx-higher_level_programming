#!/usr/bin/python3
"""
Contains the inherits from function
"""


def inherits_from(obj, a_class):
    """returns True if obj is an instance of a class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
