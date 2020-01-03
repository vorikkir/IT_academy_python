#!/usr/bin/python3.7
# -*- coding: utf-8

def pyramid(n):
    """Вычисляет сумму всех чисел на n-ом уровне"""
    num_sum = n ** 3

    return num_sum

if __name__ == '__main__':
    print(pyramid(int(input())))


# Вариант 2 -----------Почему при проверке большого числа выдает inf в втором варианте? Остальные проверки прошел.
# Перекопал интернет и так ничего не нашел, как побороть inf.


# def pyramid(n):
# #     """Вычисляет сумму всех чисел на n-ом уровне"""
# #     # Вычисляем первый и последний элементы ряда n
# #     elem_first_row = n ** 2 - (n - 1)
# #     print(elem_first_row)
# #     elem_end_row = n ** 2 + (n - 1)
# #     print(elem_end_row)
# #     # Находим порядковый номер последнего элемента в ряду n
# #     num_elen_end = (elem_end_row - elem_first_row + D) / D
# #     print(num_elen_end)
# #     # Вычисляем сумму всех элементов в ряду
# #     sum_all_elem = (elem_first_row + elem_end_row) / 2 * num_elen_end
# #     print(sum_all_elem)
# #     return sum_all_elem
# #
# # if __name__ == '__main__':
# #     print(pyramid(int(input())))