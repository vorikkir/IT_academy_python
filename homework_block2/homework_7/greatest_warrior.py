#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class Warrior:

    def __init__(self):
        """Конструктор объектов класса"""
        self.level = 1
        self.rank = "Pushover"
        self.RANK = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror",
                     "Champion", "Master", "Greatest"]
        self.experience = 100
        self.achievements = []

    def experience_change(self, experience):
        """Изменение(определение) опыта, уровня и ранга"""
        if self.experience + experience <= 10000:
            self.experience = self.experience + experience
            self.level = self.experience // 100
            self.rank = self.RANK[self.level // 10]
        else:
            self.level = 100
            self.experience = 10000
            self.rank = self.RANK[self.level // 10]

    def war(self, rival_level):
        """Генерирует сражение"""
        if rival_level > 100 or rival_level < 1:
            return "Invalid level"
        elif self.level == rival_level:
            self.experience_change(10)
            return "A good fight"
        elif self.level - 1 == rival_level:
            self.experience_change(5)
            return "A good fight"
        elif self.level - 2 >= rival_level:
            return "A good fight"
        elif int(rival_level / 10 > self.level / 10) and rival_level >= self.level + 5:
            return "You've been defeated"
        elif rival_level - 1 >= self.level:
            diff = rival_level - self.level
            self.experience_change(20 * diff * diff)
            return "An intense fight"

    def training(self, rival_training):
        """Режим тренировки"""
        if self.level >= rival_training[2]:
            self.experience_change(rival_training[1])
            self.achievements.append(rival_training[0])
            return rival_training[0]
        else:
            return "Not strong enough"


if __name__ == "__main__":
    bruce_lee = Warrior()
    print("\t*******Первоначальные характеристики война*******")
    print("Уровень воина: " + str(bruce_lee.level) + "\t\t"
          + "Опыт воина: " + str(bruce_lee.experience) + "\t\t"
          + "Ранг воина: "  + str(bruce_lee.rank) +  "\t\t"
          + "Достижения воина: " + str(bruce_lee.achievements))

    print("\n\t\t\t\t*******Тренировка*******")
    print("\n\t*******Характеристика воина после тренировки*******")
    print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]))
    print("Уровень воина: " + str(bruce_lee.level) + "\t\t"
          + "Опыт воина: " + str(bruce_lee.experience) + "\t\t"
          + "Ранг воина: " + str(bruce_lee.rank) + "\t\t"
          + "Достижения воина: " + str(bruce_lee.achievements))

    print("\n\t\t\t\t*******Сражение*******")
    print(bruce_lee.war(90))
    print("\n\t*******Характеристика воина после сражения*******")
    print("Уровень воина: " + str(bruce_lee.level) + "\t\t"
          + "Опыт воина: " + str(bruce_lee.experience) + "\t\t"
          + "Ранг воина: " + str(bruce_lee.rank) + "\t\t"
          + "Достижения воина: " + str(bruce_lee.achievements))
