#!/usr/bin/python3
"""File: 3-square.py
Author: Miguel
"""


class Square:
    """Square class with private attribute and optional instation.
    With a public instance method that\
            Returns: the current square area
    """
    def __init__(self, size=0):
        """Initialize data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the square area"""
        return self.__size ** 2
