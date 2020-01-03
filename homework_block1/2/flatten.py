#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from functools import reduce

def flatten(lists):
    """Программа, принимающая зубчатый массив любого типа и возвращающего его "плоскую" копию"""
    return reduce(lambda res, x: res + (flatten(x) if isinstance(x, list) else [x]), lists, [])

if __name__ == '__main__':
    print(flatten([1, 2, [3, 4, [5, 6], 7], [8, [9, [10]]]]))
