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

    def area(self):
        """ area of a rectangle """
        return self.__height * self.__width

    def __str__(self):
        """ prints description """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
