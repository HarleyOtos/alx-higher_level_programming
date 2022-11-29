#!/usr/bin/python3
for combine in range(0, 100):
    s1 = combine / 10
    s2 = combine % 10
    if s1 < s2 and s1 != s2 and combine != 89:
        print('{:02d}, '.format(combine), end='')
        if combine == 89:
            print('{}'.format(combine))
