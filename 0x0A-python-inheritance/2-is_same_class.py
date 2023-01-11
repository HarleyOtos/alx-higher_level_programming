#!/usr/bin/python3
"""
A module to return instance depending on the conditions fulfill
"""


def is_same_class(obj, a_class):
    """
    Checks if `obj` is an instance of the specified class

    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object

    Returns:
        `True` if the object is an instance of the
        specified class; otherwise `False`
    """

    if type(obj) == a_class:
        return True

    return False
