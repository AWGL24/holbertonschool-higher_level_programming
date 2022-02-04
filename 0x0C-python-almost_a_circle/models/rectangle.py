#!/usr/bin/python3
""" Module holds class Rectangle that inherist from Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor of rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width is not of type integer")
        elif value <= 0:
            raise ValueError("width is smaller than 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height is not of type integer")
        elif value <= 0:
            raise ValueError("height is smaller than 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x is not of type integer")
        elif value < 0:
            raise ValueError("x is smaller than 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y is not of type integer")
        elif value < 0:
            raise ValueError("y is smaller than 0")
        else:
            self.__y = value
