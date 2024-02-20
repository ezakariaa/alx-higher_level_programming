#!/usr/bin/python3
"""  Class that inherits from the built-in list """


class MyList(list):
    """ Class that inherits from list """

    def print_sorted(self):
        """ prints the list sorted in ascending order. """
        print(sorted(self))
