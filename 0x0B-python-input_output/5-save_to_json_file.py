#!/usr/bin/python3
"""function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (any): Python object.
        filename (str): The name of the file
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
