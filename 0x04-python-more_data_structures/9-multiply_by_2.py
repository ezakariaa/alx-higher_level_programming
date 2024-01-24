#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mydict = dict(a_dictionary)
    for x, y in mydict.items():
        mydict[x] = y * 2
    return mydict
