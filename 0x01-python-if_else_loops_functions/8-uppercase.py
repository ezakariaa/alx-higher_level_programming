#!/usr/bin/python3

def uppercase(str):
    '''Function prints a string in uppercase followed by a new line'''
    for lettre in str:
        if ord(lettre) >= 97 and ord(lettre) <= 122:
            lettre = chr(ord(lettre) - 32)
        print("{}".format(lettre), end='')
    print("")
