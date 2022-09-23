#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {
        '1a': 20,
        '1b': 24,
        '6a': 15,
        '7B': 10
    }
    print("Начальный вид классов и учеников:", '\n', school)
    # Изменение в 1b классе
    school['1b'] = 21
    # Новый класс
    school['2b'] = 16
    # Класс был расформирован
    del school['7B']
    S = sum(school.values())
    print('\n', school, '\n', "Общее количество учеников в школе :", S)

