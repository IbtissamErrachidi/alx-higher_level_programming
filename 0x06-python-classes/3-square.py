#!/usr/bin/python3
""" a class named Square """


class Square:
    """initialition of a Square object."""
    def __init__(self, size=0):
        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate and return the area of the square."""
        area = self.__size ** 2
        return (area)
