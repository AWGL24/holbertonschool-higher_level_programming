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
            raise TypeError("value is not of type integer")
        elif value <= 0:
            raise ValueError("value is smaller than 0")
        else:
            self.value = value
