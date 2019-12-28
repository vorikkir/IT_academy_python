#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


from datetime import datetime


def time(func):
    """Вычисляет время работы скрипта"""
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        print(datetime.now() - start)
        return result
    return wrapper


def memoize(func):
    """Запоминает результаты прошлых вызовов"""
    memory = {}

    def inner(*args):
        if args in memory:
            return memory[args]
        else:
            memory[args] = func(*args)
            return memory[args]
    return inner


@time
@memoize
def get_factorial(n):
    count = 1
    for i in range(1, n):
        count *= i
    return count


if __name__ == "__main__":
    print(get_factorial(10 ** 4))
    print(get_factorial(10 ** 4))

