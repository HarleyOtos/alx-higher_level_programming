#!/usr/bin/python3
"""
A module that prints a text with 2 new lines
after each of these characters `.`, ` `?` and `:`
"""

def text_indentation(text):
    """
    Prints a text with indentation

    Args:
        text (str): The text to prints.

    Raises:
        TypeError: If `text` isn't string.
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    text_length = len(text)
    i = 0
    new_string = ''
    starting = True

    while i < text_length:
        if text[i] == ' ' and starting is True:
            i += 1
            continue

        starting = False

        if text[i] in '.?:':
            new_string += text[i]
            new_string += '\n'
            new_string += '\n'
            i += 1

            while i < text_length and text[i] == ' ':
                i += 1

            continue
        
        if i < text_length:
            new_string += text[i]
            i += 1

    print(new_string, end='')
