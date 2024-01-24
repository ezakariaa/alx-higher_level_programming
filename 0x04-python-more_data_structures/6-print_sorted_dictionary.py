#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    j = sorted(a_dictionary)
    for i in j:
        print("{}: {}".format(i, a_dictionary[i]))
