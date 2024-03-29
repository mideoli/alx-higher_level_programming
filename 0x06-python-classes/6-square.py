#!/usr/bin/python3
"""File: 3-square.py
Author: Miguel
"""


class Square:
    """Square class with private attribute and optional instantiation.
    With a public instance method that\
            Returns: the current square area
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize data"""
        self.__size = size
        self.position = position

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
        """if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
                """
        if self.__size <= 0:
            print()
            return
        for row in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print('#', end='')
            print()

    @property
    def position(self):
        """Retrieve position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets position and handles errors"""
        if len(value) < 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
