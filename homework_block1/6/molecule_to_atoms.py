#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


import re
from collections import Counter


def calculation_molecules(chem_form):
    """Возвращает атомы из молекулы и их количество"""
    total = Counter()
    for elem, num in re.findall(regular_exp, chem_form):
        num = int(num) if num else 1
        if elem[0] in '[({':
            for key, value in calculation_molecules(elem[1:-1]).items():
                total[key] += num * value
        else:
            total[elem] += num
    result = {}
    for key, value in total.items():
        result[key] = value
    return result


if __name__ == '__main__':
    regular_exp = (r'('r'[A-Z][a-z]?'r'|'r'\([^(]+\)'r'|'r'\[[^[]+\]'r'|'r'\{[^}]+\}'r')'r'(\d*)')
    print(calculation_molecules("H2O"))
    print(calculation_molecules("Mg(OH)2"))
    print(calculation_molecules("K4[ON(SO3)2]2"))


