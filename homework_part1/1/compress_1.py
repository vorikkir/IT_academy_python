#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

COMP = [4, 0, 5, 0, 3, 0, 0, 5]  #[4, 0, 5, 0, 3, 0, 0, 5]

if __name__ == '__main__':
    COMP.sort(key=lambda x: not x)
    print(COMP)
