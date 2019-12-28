#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

#Программа, которая выводит возможность покупки мороженного порциями 3 и 5 шариков

PORTION_BALL_3 = 3
PORTION_BALL_5 = 5

if __name__ == '__main__':
    all_ice_cream = int(input("Введите порцию мороженного в шариках:\t"))
    if all_ice_cream < 10:
        if (all_ice_cream % 3 == 1 or all_ice_cream % 3 == 2) and (all_ice_cream % 5 == 1 or
                                                                    all_ice_cream % 5 == 2 or all_ice_cream % 5 == 4):
            print("No")
        else:
            print("Yes")
    else:
        print("Yes")