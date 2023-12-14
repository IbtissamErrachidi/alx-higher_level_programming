#!/usr/bin/python3
"""Define a class named Square"""


class Square:
    """ initialization of a Square object."""
    def __init__(self, size=0):
        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
