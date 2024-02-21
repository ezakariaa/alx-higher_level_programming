#!/usr/bin/python3
"""Defines class_to_json"""


def class_to_json(obj):
    """function returns the dictionary description with simple data structure"""
    return obj.__dict__
