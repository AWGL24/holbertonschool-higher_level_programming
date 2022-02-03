#!/usr/bin/python3
""" Module holds function that indents text """


def text_indentation(text):
    """ prints indented text """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        space = 1
        for ch in text:
            if ch == " " and space == 1:
                continue
            print(ch, end="")
            space = 0
            if ch in [".", "?", ":"]:
                print("\n")
                space = 1
