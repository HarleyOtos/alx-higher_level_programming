#!/usr/bin/python3
"""
A calss of BaseGeometry
"""


class BaseGeometry:
    """
    A public instance method that raises an exception
    """
    def area(self):
        """
        Raise an Exception message if area not implemented
        """

        raise Exception('area() is not implemented')
