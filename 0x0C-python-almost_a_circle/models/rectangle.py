#!/usr/bin/python3
""" class rectangle """
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
            self.__height = value

    @property
    def x(self):
        """gets the value x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value x"""
            self.__x = value

    @property
    def y(self):
        """gets the value y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value y"""
            self.__y = value
