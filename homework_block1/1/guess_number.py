#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import random

if __name__ == '__main__':
    name_game = "Игра \" Угадай число \"\n"
    print(name_game.upper().center(120))
    print("Программа произвольно выбирает число в диапазоне от 0 до 10.\n"
          "Вам необходимо его угадать за наименьшее число попыток\n")


    number = random.randint(0, 10)
    guessed_number = int(input("Угадайте число:\t"))


    counter = 1
    while True:
        if guessed_number > number:
            print("Меньше.")
            counter += 1
            guessed_number = int(input("Угадайте число:\t"))
        elif guessed_number < number:
            print("Больше.")
            counter += 1
            guessed_number = int(input("Угадайте число:\t"))
        else:
            print("Это загаданное число")
            print("Количество попыток:\t" + str(counter))
            break


