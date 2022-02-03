#!/usr/bin/python3
""" Module holds function that does a magic calculation """


def magic_calculation(a, b, c):
    """ returns magic calculation """
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
