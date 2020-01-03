#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


def bit_difference():
    """Вычисляет количество бит, которые надо поменять,
    чтобы сделать из числа A число B"""

    numbers = input("Введите два числа через зяпятую: ")
    a_num, b_num = [int(n) for n in numbers.split(',')]
    a_bin = bin(a_num)[2:].zfill(8).replace("", " ")
    b_bin = bin(b_num)[2:].zfill(8).replace("", " ")
    differ = bin(a_num ^ b_num).count("1")
    print(f"{a_num}\t{a_bin}\n{b_num}\t{b_bin}\nAnswer: {differ}")
    return differ


if __name__ == '__main__':
    bit_difference()
