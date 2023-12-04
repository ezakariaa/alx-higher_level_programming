#!/usr/bin/python3


def no_c(my_string):
    output = my_string.translate({ord(l): None for l in 'cC'})
    return output
