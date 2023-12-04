#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    for l in range(len(my_list)):
        if my_list[l] % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist
