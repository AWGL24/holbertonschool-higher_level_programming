#!/usr/bin/python3
""" Module holds function that writes a file """


def write_file(filename="", text=""):
    """ writes on a file """

    with open(filename, 'w', encoding="utf-8") as My_file:
        My_file.write(text)
        return len(text)
