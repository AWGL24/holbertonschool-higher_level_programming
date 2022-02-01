#!/usr/bin/python3
""" Module holds function that writes a file """


def write_file(filename="", text=""):
    """ writes on a file

            param:
            filename="": name of the file
            text="": text to be writed
    """
    with open(filename, mode="w", encoding="utf-8") as My_file:
        My_file.write(text)
