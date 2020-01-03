#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from collections import Counter


def selections(*selection):
    list_selection = []
    for i in selection:
        for j in i:
            list_selection.append(j)

    vote_min = len(list_selection) / 2
    calc_candidate = Counter(list_selection)
    slice_candid = calc_candidate.most_common(2)
    if slice_candid[0][1] > vote_min:
        winner = slice_candid[0][0]
        print(winner)
        return winner
    else:
        total = []
        for i in slice_candid:
            for j in i:
                if str(j).replace(' ', '').isalpha():
                    total.append(j)
        print(tuple(total))
        return total


if __name__ == '__main__':
    # selections(["Полуэкт Варфоломеев", "Варфоломей Виссарионов",
    #             "Виссарион Полуэктов", "Варфоломей Виссарионов",
    #             "Варфоломей Виссарионов", "Полуэкт Варфоломеев",])
    selections(["Полуэкт Варфоломеев", "Варфоломей Полуэктов", "Полуэкт Варфоломеев",])
