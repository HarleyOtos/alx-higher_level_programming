#!/usr/bin/python3
"""
A function to return an object 
"""

import json


def from_json_string(my_str):
    """
    function that returns an Python data represented by a JSON
    """

    return json.loads(my_str)
