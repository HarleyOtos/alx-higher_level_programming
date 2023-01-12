#!/usr/bin/python3
"""
A function to return an object 
"""

from json import loads


def from_json_string(my_str):
    """
    function that returns an Python data represented by a JSON
    """
    return loads(my_str)
