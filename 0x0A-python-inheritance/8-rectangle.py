#!/usr/bin/python3
""" Module holds BaseGeometry import """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle inherits BaseGeometry """

    def __init__(self, width, height):
        """ Instantation """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
