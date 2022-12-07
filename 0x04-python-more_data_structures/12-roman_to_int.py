#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_letters = [
        ['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100],
        ['D', 500], ['M', 1000]
    ]
    num = 0
    last = 0

    for letter in roman_string:
        for i in roman_letters:
            if letter == i[0]:
                if last == 0 or last >= i[1]:
                    num += i[1]
                elif last < i[1]:
                    num += i[1] - (last * 2)
                last = i[1]
    return num
