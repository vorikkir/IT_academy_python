#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


import random


cards = {"2♦": 2, "3♦": 3, "4♦": 4, "5♦": 5, "6♦": 6, "7♦": 7, "8♦": 8, "9♦": 9, "10♦": 10, "J♦": 10, "Q♦": 10,
         "K♦": 10, "A♦": 11, "2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7, "8♥": 8, "9♥": 9, "10♥": 10,
         "J♥": 10, "Q♥": 10, "K♥": 10, "A♥": 11, "2♠": 2, "3♠": 3, "4♠": 4, "5♠": 5, "6♠": 6, "7♠": 7, "8♠": 8,
         "9♠": 9, "10♠": 10, "J♠": 10, "Q♠": 10, "K♠": 10, "A♠": 11, "2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5, "6♣": 6,
         "7♣": 7, "8♣": 8, "9♣": 9, "10♣": 10, "J♣": 10, "Q♣": 10, "K♣": 10, "A♣": 11
         }


def first_distribution():
    """Первая раздача карт"""
    for i in range(2):
        a = random.choice(list(cards.keys()))
        my_cards.append(cards[a])
        print(a, end=" ")
        del cards[a]
        my_points = sum(map(lambda x: x, my_cards))
        if my_points == 22:
            my_cards[1] = 1
    print("\nКарты диллера")

    for i in range(1):
        a = random.choice(list(cards.keys()))
        dealer_cards.append(cards[a])
        print(a, end=" ")
        del cards[a]


def plus_one_card_player():
    """Раздает одну карту игроку"""
    for i in range(1):
        a = random.choice(list(cards.keys()))
        my_cards.append(cards[a])
        my_points = sum(map(lambda x: x, my_cards))
        if my_points > 21 and cards[a] == 11:
            my_cards[-1] = 1
        del cards[a]
        print("Вы получили карту: ", a)


def plus_one_card_dealer():
    """Раздает одну карту диллеру"""
    for i in range(1):
        a = random.choice(list(cards.keys()))
        dealer_cards.append(cards[a])
        dealer_points = sum(map(lambda x: x, dealer_cards))
        if dealer_points > 21 and cards[a] == 11:
            dealer_cards[-1] = 1
        del cards[a]
        print("Диллер получили карту: ", a)


def player_have_black_jack():
    """Когда у игрока black jack"""
    dealer_points = sum(map(lambda x: x, dealer_cards))
    if dealer_points == 21:
        print("Ровно. Все остаются при своих ставках")
    elif dealer_points < 21:
        plus_one_card_dealer()
        player_have_black_jack()
    else:
        print("Вы выйграли")


def cards_dealer():
    """Дополнительные карты диллера"""
    my_points = sum(map(lambda x: x, my_cards))
    dealer_points = sum(map(lambda x: x, dealer_cards))
    if dealer_points > my_points and dealer_points <= 21:
        print("Диллер выйграл")
    elif dealer_points == my_points:
        print("Ровно. Все остаются при своих ставках")
    elif dealer_points < my_points and dealer_points < 21:
        plus_one_card_dealer()
        cards_dealer()
    elif dealer_points > 21:
        print("Вы выйграли")


def cards_player():
    """Дополнительные карты игрока"""
    my_points = sum(map(lambda x: x, my_cards))
    if my_points > 21:
        print("Перебор")
        print("Игра окончена")
    elif my_points == 21:
        player_have_black_jack()
    else:
        print("Ваши действия?(Введите Y, если хотите еще карту. Иначе N)")
        action = input(">>> ")
        if action.lower() == "y":
            plus_one_card_player()
            cards_player()
        else:
            cards_dealer()


if __name__ == '__main__':
    my_cards = []
    dealer_cards = []
    stake = input("Введите ставку: ")
    print("Начинаю раздачу:")
    print("Ваши карты")
    first_distribution()
    my_points = sum(map(lambda x: x, my_cards))
    dealer_points = sum(map(lambda x: x, dealer_cards))
    print()
    if my_points == 21:
        print(f"Вы выйграли, ваш приз составил\t{int(stake) * 1.5}")
    elif my_points > 21:
        print("Перебор")
        print("Игра окончена")
    elif my_points < 21:
        cards_player()
