#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""Напишите функцию, принимающую строку - число записанное при помощи
 римских цифр и возвращающее int - значение этого числа в 10-ричной системе

Пример
1. roman("MCMXC") -> 1990
2. roman("MMVIII") -> 2008
3. roman("MDCLXVI") -> 1666
"""

ROMAN_NUMBER = {"I": 1, "V": 5, "X": 10, "L": 50, "XC": 90,
                "C": 100, "D": 500, "CM": 900, "M": 1000}


def counter_arab_num():
    arab_num = 0
    rom_nums = input(">>> Введите римское число:\t").upper()
    for rom_num in rom_nums:
        if rom_num in ROMAN_NUMBER:
            arab_num += ROMAN_NUMBER[rom_num]
    # Выполняем проверку наличия "CM" or "XC" в римском числе
    if "CM" or "XC" in rom_nums:
        num_cm = "CM"
        num_xc = "XC"
        for key, value in ROMAN_NUMBER.items():
            if key == num_cm and num_cm in rom_nums:
                arab_num += ROMAN_NUMBER[key]
                arab_num -= ROMAN_NUMBER["C"] + ROMAN_NUMBER["M"]
            if key == num_xc and num_xc in rom_nums:
                arab_num += ROMAN_NUMBER[key]
                arab_num -= ROMAN_NUMBER["X"] + ROMAN_NUMBER["C"]
    return arab_num


if __name__ == '__main__':
    print(counter_arab_num())




# # Вариант без проверки двойных чисел
# arab_num = 0
# rom_nums = input(">>>ВВедите римское число:\t").upper()
# for rom_num in rom_nums:
#     if rom_num in ROMAN_NUMBER:
#         arab_num += ROMAN_NUMBER[rom_num]
# print(arab_num)
