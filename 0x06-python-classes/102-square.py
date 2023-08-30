#!/usr/bin/python3
"""File: 102-square.py
Author: Miguel
"""


class Square:
    """
    Defines a square.

    Attributes:
        size (float or int): The size of the square's sides.
    """

    def __init__(self, size=0):
        """
        Initialize a square.

        Args:
            size (float or int): The size of the square's sides (default is 0).
        """
        self.size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Implement the equality comparator (==) based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Implement the inequality comparator (!=) based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Implement the greater-than comparator (>) based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Implement the greater-than-or-equal comparator (>=)\
                based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Implement the less-than comparator (<) based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Implement the less-than-or-equal comparator (<=) based on square areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area is less or equal, False otherwise.
        """
        return self.area() <= other.area()

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square and handle errors.

        Args:
            value (float or int): The new size for the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
