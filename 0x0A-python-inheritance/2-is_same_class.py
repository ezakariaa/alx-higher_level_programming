#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """returns True if object is exactly of specified class; otherwise False"""
    return (type(obj) == a_class)
