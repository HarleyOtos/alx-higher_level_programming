#!/usr/bin/python3
"""
A function that appends a string at the end of text file
"""


def append_write(filename="", text=""):
    """ function that appends a string returns the number of characters """

    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
