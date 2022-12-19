#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    try:
        idx = 0
        for i in my_list:
            if idx < x:
                print('{}'.format(i), end='')
                idx += 1
        print('')
        return idx
    except SyntaxError:
        print('Error Syntax')

