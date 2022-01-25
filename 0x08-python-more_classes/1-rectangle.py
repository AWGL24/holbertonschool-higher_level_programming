#!/usr/bin/python3
""" Module with the class Rectangle """


class Rectangle:
    """ Rectangle Defined"""
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """ Docstring of __init___ method
        Args:
            width (int): size from main to be displayed
            height (int): size from main to be displayed
        """
        self.__height = height
        self.__width = width
        """ int: Docstring *after* attribute, with type specified """

    @property
    def width(self):
        """ Docstring of width """
        return self.__width
        """ returns the width attribute with value """

    @width.setter
    def width(self, value):
        """ Docstring of width
        Args:
            value (int): contains size from __width attribute
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        """ set width """

    @property
    def height(self):
        """ Docstring of height """
        return self.__height
        """ returns the height attribute with value """

    @height.setter
    def height(self, value):
        """ Docstring of height
        Args:
            value (int): contains size from __height attribute
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
        """ set height """
