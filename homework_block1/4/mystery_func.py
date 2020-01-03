# !/usr/bin/python3.7
# -*- coding: utf-8 -*-


def mystery(n):
    """Function gray"""
    arr = []
    for i in range(0, 1 << n):
        num = i ^ (i >> 1)
        arr.append("{0:0{1}b}".format(num, n))
    return int(arr[n], 2)


if __name__ == '__main__':
    print(mystery(6))


# def mystery_inv(n):
#     """Function gray"""
#     arr = []
#     for i in range(0, 1 << n):
#         num = i ^ (i >> 1)
#         arr.append("{0:0{1}b}".format(num, n))
#     total = int(arr[n - 1], 2)
#     return total
#
#
# if __name__ == '__main__':
#     print(mystery_inv(6))
