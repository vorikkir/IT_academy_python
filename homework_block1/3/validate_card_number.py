#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


def validate(card):
    """Принимает 16-значное число - номер кредитной карты
     и проверяющей может ли такая картa существовать."""

    numbers = [int(i) for i in str(card)]
    total = 0
    for index, num in enumerate(numbers):
        if index % 2 == 0:
            if numbers[index] * 2 > 9:
                total += num * 2 - 9
            else:
                total += num * 2
        else:
            total += num

    return total % 10 == 0




if __name__ == '__main__':
    print(validate(4561261212345464))
    # print(validate(4561261212345467))
