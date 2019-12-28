#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


def calculating_ip(number):
    """Принимает целочисленное число до 32 бит и возвращает строку
     - представление этого числа в виде IPv4 адреса"""

    num_bin = bin(number)[2:].zfill(32)
    first_octet = str(int(num_bin[0:8], 2))
    second_octet = str(int(num_bin[8:16], 2))
    third_octet = str(int(num_bin[16:24], 2))
    fourth_octet = str(int(num_bin[24:32], 2))
    result = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
    return result


if __name__ == '__main__':
    print(calculating_ip(2149583361))
    # print(calculating_ip(32))
    # print(calculating_ip(0))
