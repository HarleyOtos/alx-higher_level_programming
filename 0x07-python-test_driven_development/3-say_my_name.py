#!/usr/bin/python3
"""
A module that print a name of anything
The output returns first and last name.
 * The first name and last name must be strings
"""

def say_my_name(first_name, last_name=""):
    """
    A function to print names

    Args:
        first_name (str): The first name of anything.
        last_name (str): The last name of anything.

    Raises:
        TypeError: If `first_name` and `last_name` aren't strings.
    """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is', first_name, last_name)
