#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


def snail(a):
    """Функция, которая бы преобразовывает двумерный массив в одномерный "Улиткой" """
    return list(a[0])+snail(list(zip(*a[1:]))[::-1])if a else []

if __name__ == '__main__':
    a = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    print(snail(a))