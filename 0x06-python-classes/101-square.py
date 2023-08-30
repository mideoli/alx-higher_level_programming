#!/usr/bin/python3
"""File: 101-square.py
Author: Miguel
"""


class Square:
    """
    Defines a square.

    Attributes:
        size (int): The size of the square's sides.
        position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square.

        Args:
            size (int): The size of the square's sides (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character to stdout.

        If the size is 0, an empty line is printed.
        """
        if self.__size <= 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square and handle errors.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square and handle errors.

        Args:
            value (tuple): The new position for the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If any value in the tuple is less than 0.
        """
        if len(value) < 2 or not all(isinstance(val, int) for val in value):
            raise ValueError('position must be a tuple of 2 positive integers')
        if any(val < 0 for val in value):
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = value

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        if self.__size == 0:
            return ""

        new_str = ""
        for _ in range(self.__position[1]):
            new_str += '\n'
        for _ in range(self.__size):
            new_str += ' ' * self.__position[0] + '#' * self.__size + '\n'
        return new_str.rstrip()  # Remove trailing newline
