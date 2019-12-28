#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


def get_prime_generator():
    """Функция возвращает по требованию простые числа"""
    primes = [2]
    yield 2
    num = 3
    while True:
        for i in primes:
            if num % i == 0:
                num += 1
                break
        else:
            primes.append(num)
            yield num


if __name__ == "__main__":
    prime = get_prime_generator()
    print(prime)
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
