#!/usr/bin/python3
""" Module has function that checks for the instance of a class """


def inherits_from(obj, a_class):
    """ returns True/False if obj is instance of a class
        that inherited specified class """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
