#!/usr/bin/python3
"""
A module use to divide matrix of element.

This module handles the division of all the values of a matrix
in line with the divisor pass by the user. In other for the
program to function properly, few consideration must be noted:

    * The matrix must be a list of integers or floats.
    * The divisor must be a number integer or float other than 0.
    * Each row of the matrix must be of the same size.
    * The result is delivered in a new matrix.
    * Division of all the elements of the matrix is rounded to 2
    decimal places.
"""

def matrix_divided(matrix, div):
    """A function to divides all elements of a matrix.

    It takes cares of the data sent by the user to verify that the
    matrix contains lists within it and that each list has integer or float.
    The result of the splitting opereation will be added to a new list
    in a new matrix with the same matrix structure as given.

    In situation were the format of the matrix is incorrect or
    the divisor is not a number, this function will raise an error.

    Args:
        matrix (:obj:`list` of :obj:`list`): The matrix to be divided.
        div (int): The divisor number.

    Returns:
        list: A new matrix with all elements divided.

    Raises:
        TypeError: If the `matrix` list of lists of integers or floats
            or if `div` is not a number.
        ZeroDivisionError: If `div` is equal to `0`.

    """

    find_list(matrix)
    find_divisor(div)

    elem_sizes = set()
    new_list = list()

    for elem in matrix:
        if find_list(elem) is False:
            raises_matrix_type_error()

        elem_sizes = check_row_size(elem_sizes, elem)
        values = []

        for value in elem:
            if find_number(value) is False:
                raises_matrix_type_error()

            values.append(round(value / div, 2))

        new_list.append(values)

    return new_list

def find_list(value):
    """
    Check if the value is of type list

    Args:
        value (any): The value to verify.

    Raises:
        TypeError: If the `value` isn't a list.
    """

    if type(value) is not list or len(value) == 0:
        raises_matrix_type_error()

def find_divisor(div):
    """
    Check if the divisor is integer, float or zero

    Args:
        div (any): The divisor to verify.

    Raises:
        TypeError: If `value` isn't integer or float.
        ZeroDivisionError: If `div` is equal to `0`.
    """

    if find_number(div) is False:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

def find_number(value):
    """
    Check that the value is integer or float

    Args:
        value (any): The value to verify.

    Returns:
        bool: True if successful, False on fail
    """

    if type(value) is not int and type(value) is not float:
        return False

    """Check for NaN value"""
    if value != value:
        return False

    return True

def check_row_size(elem_sizes, row):
    """
    Check the size consistency of rows in a matrix

    Check if all rows in the matrix are inconsitently sized

    Args:
        elem_sizes (:obj:`set` of :obj:`int`): Size of each row matrix.
        row (list): A row with elements to divide.

    Returns:
        set: A unique consistent size between all rows.

    Raises:
        TypeError: If `elem_sizes` has more than one size
        in its contents.
    """

    elem_sizes.add(len(row))

    if len(elem_sizes) > 1:
        raise TypeError('Each row of the matrix must have the same size')
    return elem_sizes

def raises_matrix_type_error():
    """
    Raises a matrix TypeError

    Raises:
        TypeError: If `matirx` list of lists of integers or floats.
    """

    raise TypeError('matrix must be a matrix \ (list of lists) of integers/floats')
