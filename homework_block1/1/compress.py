#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

COMP = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


if __name__ == '__main__':
    for i in reversed(range(len(COMP))):
        if i == 0:
            break
        if COMP[i] != 0 and COMP[i - 1] == 0:
            a = COMP[i]
            b = COMP[i - 1]
            c = b
            COMP[i - 1] = a
            COMP[i] = c
        if COMP[i] != 0 and COMP[i - 1] != 0 and COMP[abs(i - 2)] == 0:
            a = COMP[i - 2]
            b = COMP[i - 1]
            c = b
            COMP[i - 1] = a
            COMP[i - 2] = c
            a = COMP[i]
            b = COMP[i - 1]
            c = b
            COMP[i - 1] = a
            COMP[i] = c
        if COMP[i] != 0 and COMP[i - 1] != 0 and COMP[i - 2] != 0 and COMP[abs(i - 3)] == 0:
            a = COMP[i - 2]
            b = COMP[i - 3]
            c = b
            COMP[i - 3] = a
            COMP[i - 2] = c
            a = COMP[i - 1]
            b = COMP[i - 2]
            c = b
            COMP[i - 2] = a
            COMP[i - 1] = c
            a = COMP[i]
            b = COMP[i - 1]
            c = b
            COMP[i - 1] = a
            COMP[i] = c
    print(COMP)
