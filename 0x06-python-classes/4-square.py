#!/usr/bin/python3
"""class square"""


class Square:
    """private instance and raise errors for exception"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """returns the squarea area"""
        return self.__size ** 2
