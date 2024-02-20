#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file.

    Args:
        filename (str): The name of the file to read.
        text (str): The text to append
    Return:
        returns the number of characters written
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
