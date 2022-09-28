#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список студентов.
    students = []
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("select - запросить студентов с баллом выше 4.0;")
    print("exit - завершить работу с программой.")

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о студенте.
            name = input("Фамилия и инициалы? ")
            group = input("Номер группы? ")
            progress = [
                int(input("Оценка за 1 семестр")),
                int(input("Оценка за 2 семестр")),
                int(input("Оценка за 3 семестр")),
                int(input("Оценка за 4 семестр")),
                int(input("Оценка за 5 семестр"))
            ]
            # Создать словарь.
            student = {
                'name': name,
                'group': group,
                'mark': progress
            }
            # Добавить словарь в список.
            students.append(student)
            if len(students) > 1:
                students.sort(key=lambda item: item.get('group')[::-1])

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Группа",
                    "Успеваемость"
                )
            )
            print(line)

            # Вывести данные о всех студентах.
            for idx, student in enumerate(students, 1):
                ma = student.get('mark', '')
                print(
                    '| {:^4} | {:<30} | {:<20} | {}.{}.{}.{}.{:<7} |'.format(
                        idx,
                        student.get('name', ''),
                        student.get('group', ''),
                        ma[0],
                        ma[1],
                        ma[2],
                        ma[3],
                        ma[4]
                    )
                )
            print(line)

        elif command.startswith('select'):
            # Инициализировать счетчик.
            count = 0
            # Проверить сведения студентов из списка.
            for student in students:
                mark = student.get('mark', '')
                if sum(mark) / max(len(mark), 1) >= 4.0:
                    print(
                        '{:>4} {}'.format('*', student.get('name', '')),
                        '{:>1} {}'.format('группа №', student.get('group', ''))
                    )
                    count += 1
            if count == 0:
                print("Студенты с баллом 4.0 и выше не найдены.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
