#!/usr/bin/python3
"""
A class that inherits from the BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class of square that inherits from the Rectangle
    """

    def __init__(self, size):
        """ The constructor """
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)
    
    def area(self):
        """ Calculator area """
        return super().area()

    def __str__(self):
        """Print the information"""
        return '[Square] {:d}/{:d}'.format(self.__size, self__size) + '/' + str(self.__size)
