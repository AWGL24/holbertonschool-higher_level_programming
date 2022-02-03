#!/usr/bin/python3
""" Module holds class that inherits from int """


class MyInt(int):
    """ inherits from int """

    def __eq__(self, other):
        """ reverses eq logic """
        return (self.real != other.real) or (self.imag != other.imag)

    def __ne__(self, other):
        """ reverses ne logic """
        return (self.real == other.real) and (self.imag == other.imag)
