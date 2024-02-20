#!/usr/bin/python3
"""function that returns an object (Python data structure)"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string

    Args:
        my_str (str): JSON string.
    """
    return json.loads(my_str)
