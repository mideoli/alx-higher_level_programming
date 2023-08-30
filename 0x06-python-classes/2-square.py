#!/usr/bin/python3
class Square:
    """Square class with privat eattribute and optional instation"""
    def __init__(self, size=0):
        """Initialize data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
