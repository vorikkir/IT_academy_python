#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

def flags(number):
    for i in range(number):
        print("+___", end=" ")
    print()
    for i in range(number):
        print("|%s /" % (i + 1), end=" ")
    print()
    for i in range(number):
        print("|__\\", end=" ")
    print()
    for i in range(number):
        print("|   ", end=" ")
    print()


if __name__ == '__main__':
    flags(int(input()))
