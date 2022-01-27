#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys


def main():
    """
    Главная функция программы.
    """
    # Список работников.
    workers = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # запросить команду из терминала
        command = input(">>>").lower()

        # выполнить действие в соответствии с командой
        if command == 'exit':
            break

        elif command == 'add':
            # запрос данных пользователя
            worker = get_worker()
            # добавление словаря в список
            workers.append(worker)
            # сортировка списка в случае необходимости
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('year', ''))

        elif command == 'all':
            # Отобразить всех работников.
            display_workers(workers)

        elif command.startswith('found '):

            # разобрать команду на части для выделения номера
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый номер
            phone = (parts[1])

            # Выбрать работников с заданным стажем.
            selected = select_workers(workers, phone)
            # Отобразить выбранных работников.
            display_workers(selected)

        elif command == 'help':
            # Вывести справку о работе с программой
            print("Список команд:\n")
            print("add - добавить работника;")
            print("all - вывести список работников;")
            print("found <x-xxx-xxx-xx-xx> - найти работника по номеру;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


def get_worker():
    """
    Запросить данные о работнике.
    """
    # запрос данных пользователя
    name = input("Имя: ")
    fam = input("Фамилия: ")
    year = input("Дата рождения (yyyy.mm.dd): ")
    tel = input("Телефон: (x-xxx-xxx-xx-xx): ")

    # создать словарь
    return {
        'name': name,
        'fam': fam,
        'year': year,
        'tel': tel,
    }


def display_workers(staff):
    """
    Отобразить список работников.
    """
    # Проверить, что список работников не пуст.
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 20,
            '-' * 20,
            '-' * 12,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^20} | {:^20} | {:^12} | {:^20} |'.format(
                "№",
                "Фамилия",
                "Имя",
                "Год",
                "Телефон"
            )
        )
        print(line)

        # Вывести данные о всех сотрудниках.
        for idx, worker in enumerate(staff, 1):
            print(
                '| {:^4} | {:^20} | {:^20} | {:^12} | {:^20} |'.format(
                    idx,
                    worker.get('name', ''),
                    worker.get('fam', ''),
                    worker.get('year', ''),
                    worker.get('tel', '')
                )
            )

        print(line)
    else:
        print("Список работников пуст.")


def select_workers(staff, phone):
    """
    Выбрать работников с заданным телефоном.
    """
    result = []
    for employee in staff:
        if employee.get('tel', '') == phone:
            result.append(employee)
    # возвратить список выбранных работников
    return result
