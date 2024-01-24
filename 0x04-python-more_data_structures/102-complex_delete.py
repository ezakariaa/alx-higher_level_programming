#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())

    if value not in values:
        return a_dictionary
    else:
        for k, val in enumerate(values):
            if val == value:
                del a_dictionary[keys[k]]
    return a_dictionary
