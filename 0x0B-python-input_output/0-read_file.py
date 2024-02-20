#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
        filename (.txt): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as file:
        file_content = file.read()
        print(file_content, end="")
