#!/usr/bin/python3
""" Module holds function that reads a file """


def read_file(filename=""):
    """ reads the content of a file """

    with open(filename) as MyFile:
        print(MyFile.read(), end="")
