#!/usr/bin/python3
""" Module holds function that adds and attribute """


def add_attribute(obj, attr, val):
    """ adds attribute """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, val)
