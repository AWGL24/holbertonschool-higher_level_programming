#!/usr/bin/python3
""" Module created class that inherits """


class MyList(list):
    """ class inherits from list """

    def print_sorted(self):
        """ method prints sorted list """
        print(sorted(self))
