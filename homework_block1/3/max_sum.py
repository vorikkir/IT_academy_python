#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


def max_sum(arroy):
    """Находит наибольшую подсумму несоседних элементов массива"""
    solution = [0 for _ in arroy]
    for i, elem in enumerate(arroy):
        solution[i] = max(solution[i - 1], elem + solution[i - 2])
    return solution[-1]

if __name__ == '__main__':
    arroy = [3, 7, 4, 6, 5]
    # arroy = [-2, 1, 3, -4, 5]
    print(max_sum(arroy))
