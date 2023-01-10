#!/usr/bin/python3
"""
A module to prints a list inherents in ascending order
"""


class MyList(list):
    """
    A class to customize the list class
    """

    def print_sorted(self):
        """
        Prints a list in ascending order
        Sort the list and then prints the output
        """

        if issubclass(MyList, list):
            print(sorted(self))
