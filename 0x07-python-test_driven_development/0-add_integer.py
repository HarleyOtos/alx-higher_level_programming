#!/usr/bin/python3
"""
A module use in adding two numbers

In this module we perform additional between two numbers,
the numbers are either integers or floats.
"""

def add_integer(a, b=98):
    """Adds two numbers

    The addition between two numbers.

    Args:
        a (:obj:`int, float`): The first number to add.
        b (:obj:`int, float`, optional): The second number to add.

    Returns:
        int: The results or output of the addition perform.
    
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b

def convert_to_int(num):
    """Cast the data type of num parameter

    A function to convert a float to an integer

    Args:
        num (:obj:`int, float`): The number to cast.

    Returns:
        int: The number casted to the integer.
    """

    if type(num) is float:
        num = int(num)
        return num

    return num
