#!/usr/bin/python3
"""File: 3-square.py
Author: Miguel
"""


class Square:
    """Square class with private attribute and optional instantiation.
    With a public instance method that\
            Returns: the current square area
    """

    def __init__(self, size=0):
        """Initialize data"""
        self.__size = size

    def area(self):
        """Returns the square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves data"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size and handles errors"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with character `#`"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
