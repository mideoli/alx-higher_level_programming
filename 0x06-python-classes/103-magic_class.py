#!/usr/bin/python3
"""File: 103-magic_class.py
Author: Miguel
"""


import math

class MagicClass:
    """
    Represents a class that performs calculations based on a given radius.

    Attributes:
        __radius (float or int): The radius used for calculations.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance with a given radius.

        Args:
            radius (float or int): The radius for calculations (default is 0).

        Raises:
            TypeError: If radius is not a number (float or integer).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of a circle with the stored radius.

        Returns:
            float: The calculated area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of a circle with the stored radius.

        Returns:
            float: The calculated circumference.
        """
        return 2 * math.pi * self.__radius
