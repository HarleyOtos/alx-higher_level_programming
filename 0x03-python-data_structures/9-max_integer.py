#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    integer = my_list[0]
    for i in my_list:
        if integer < i:
            integer = i
    return integer
