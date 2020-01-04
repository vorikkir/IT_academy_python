#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


import math


class Fraction:
    """Класс поддерживает все арифметические операции над дробями"""
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        numerator_new = self.numerator * other.denominator + self.denominator * other.numerator
        denominator_new = self.denominator * other.denominator
        gcd = math.gcd(numerator_new, denominator_new)
        return Fraction(numerator_new // gcd, denominator_new // gcd)

    def __sub__(self, other):
        numerator_new = self.numerator * other.denominator - self.denominator * other.numerator
        denominator_new = self.denominator * other.denominator
        gcd = math.gcd(numerator_new, denominator_new)
        return Fraction(numerator_new // gcd, denominator_new // gcd)

    def __mul__(self, other):
        numerator_new = self.numerator * other.numerator
        denominator_new = self.denominator * other.denominator
        gcd = math.gcd(numerator_new, denominator_new)
        return Fraction(numerator_new // gcd, denominator_new // gcd)

    def __truediv__(self, other):
        numerator_new = self.numerator * other.denominator
        denominator_new = self.denominator * other.numerator
        gcd = math.gcd(numerator_new, denominator_new)
        return Fraction(numerator_new // gcd, denominator_new // gcd)


if __name__ == "__main__":
    my_fraction1 = Fraction(1, 2)
    my_fraction2 = Fraction(3, 4)
    my_fraction3 = Fraction(1, 9)
    my_fraction4 = Fraction(3, 5)
    print(my_fraction1+my_fraction2+my_fraction3*my_fraction4)

    my_fraction1 = Fraction(40, 70)
    print(my_fraction1)
