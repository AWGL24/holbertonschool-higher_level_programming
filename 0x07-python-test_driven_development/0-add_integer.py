#!/usr/bin/python3
"""

Function that adds two integers

"""


def add_integer(a, b=98):
    """ Given two integers, return the sum """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) not in [int]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int]:
        raise TypeError("b must be an integer")
    else:
        return a + b
