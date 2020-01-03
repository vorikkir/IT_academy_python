#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import time

# Случайное число в промежутке (0, 1)
"""Код получился ужасный и  не оптимальный, все никак не мог отвязаться от модуля random"""

if __name__ == '__main__':
    NUMBERS = str()
    for i in range(9):
        coun_fir = str(time.time())
        time.sleep(1 / 999)
        num = coun_fir[-1]
        NUMBERS += num
        if i == 8:
            while True:
                coun_sec = str(time.time())
                time.sleep(1 / 999)
                c = coun_sec[-1]
                random_num = int(NUMBERS) / 10 ** int(c)
                if random_num < 1:
                    break
            print(random_num)
