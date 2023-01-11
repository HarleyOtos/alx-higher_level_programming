#!/usr/bin/python3
""" 
Class that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class of square that inherits from Rectangle
    """

    def __init__(self, size):
        """ A contructor """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
