#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    
    try:
        for i in my_list:
            if a < x:
                print('{}'.format(my_list[a]), end='')
                a += 1

        print()
    except TypeError:
        pass
    finally:
        return a
