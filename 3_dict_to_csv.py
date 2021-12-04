"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
dictionary=[
    {"name": "Анна", "age":32, "job": "Архитектор"},
    {"name": "Лена", "age":29, "job": "Водитель"},
    {"name": "Иван", "age":54, "job": "Инженер"},
    {"name": "Владимир", "age":22, "job": "Строитель"},
]

with open('dict-file.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'job', 'age']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for line in dictionary:
        writer.writerow(line)

if __name__ == "__main__":
    main()
