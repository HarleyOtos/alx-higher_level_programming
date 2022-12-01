#!/usr/bin/python3
import sys

if __name__ == '__main__':
    s = sys.argv
    l_s = len(s)
    sum = 0

    if l_s > 1:
        for i in range(1, l_s):
            sum += int(s[i])
    print(sum)
