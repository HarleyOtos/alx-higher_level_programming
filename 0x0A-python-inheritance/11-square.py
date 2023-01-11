#!/usr/bin/python3
"""
A class that inherits from the BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class of square that inherits from the Rectangle
    """

    def __init__(self, size):
        """ The constructor """

        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Print the information"""
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
