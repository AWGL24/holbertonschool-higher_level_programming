#!/usr/bin/python3
""" Module holds functon that returns the dict description for JSON sterilization of an obj """


def class_to_json(obj):
    """ returns dict description for JSON """
    return obj.__dict__
