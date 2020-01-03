#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


def excess_count(arr):
    """Вычисляет непарное число"""
    total = 0
    for i in arr:
        total = total ^ i
    return total

if __name__ == '__main__':
    arr = [1, 5, 2, 9, 2, 9, 1]
    print(excess_count(arr))


# Вариант 2 -------------------------------------------------------

# def excess_count(arr):
#     """Вычисляет непарное число"""
#     for i in arr:
#         if arr.count(i) == 1:
#             break
#     return i
#
#
# if __name__ == '__main__':
#     arr = [1, 5, 2, 9, 2, 9, 1]
#     print(excess_count(arr))
