"""Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла."""

import pickle
import csv


def pickle_to_csv(file_pickle: str, file_csv: str) -> None:
    with open(file_pickle, 'rb') as p:
        new_dict = pickle.load(p)
        print(new_dict)
    with open(file_csv, 'w', newline='', encoding='utf-8') as c:
        csv_writer = csv.DictWriter(c, fieldnames=(new_dict[0].keys()), dialect='excel-tab')
        csv_writer.writeheader()
        csv_writer.writerows(new_dict)


if __name__ == '__main__':
    pickle_to_csv('task_04.pickle', 'task_06.csv')
