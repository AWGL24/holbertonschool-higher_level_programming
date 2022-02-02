#!/usr/bin/python3
""" Module holds function that returns obj represented by JSON str """
import json


def from_json_string(my_str):
    """ returns obj represented by json str """

    return json.loads(my_str)
