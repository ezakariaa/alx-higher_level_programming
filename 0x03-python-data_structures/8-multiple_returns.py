#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    first_chara = sentence[0] if length > 0 else "None"
    tupl = length, first_chara
    return(tupl)
