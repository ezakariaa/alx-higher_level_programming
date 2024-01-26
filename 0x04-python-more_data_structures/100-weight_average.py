#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avrg = 0
    div = 0
    for tup in my_list:
        avrg += tup[0] * tup[1]
        div += tup[1]
    return float(avrg / div)
