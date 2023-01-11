#!/usr/bin/python3
"""
A class that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class of Rectangle inheriting from BaseGeometry
    """

    def __init__(self, width, height):
        """The constructor"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """The calculation area"""
        return self.__width * self.__height

    def __str__(self):
        """print the information"""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
