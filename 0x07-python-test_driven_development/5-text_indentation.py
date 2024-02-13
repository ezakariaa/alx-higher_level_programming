#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Function prints text with 2 new lines after characters: ., ? and :

    Args:
        text (string): Text.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    counter = 0
    while counter < len(text) and text[counter] == ' ':
        counter += 1

    while counter < len(text):
        print(text[counter], end="")
        if text[counter] == "\n" or text[counter] in ".?:":
            if text[counter] in ".?:":
                print("\n")
            counter += 1
            while counter < len(text) and text[counter] == ' ':
                counter += 1
            continue
        counter += 1
