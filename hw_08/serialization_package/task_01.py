"""Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов."""

import csv
import json
import pathlib
import pickle
from os import path, walk


def inspect_dir(directory: str,
                file_json: str = 'dir_info.json', file_csv: str = 'dir_info.csv', file_pickle: str = 'dir_info.pickle'):
    new_dict_list = []
    for dir_path, dir_names, file_names in walk(directory):
        for folder in dir_names:
            folder_size = 0
            for folder_path, folders, files in walk(f'{dir_path}/{folder}'):
                for file in files:
                    file_path = path.join(folder_path, file)
                    folder_size += path.getsize(file_path)
            new_dict_list.append({
                'object_name': folder,
                'parent_directory': dir_path,
                'object_type': 'folder',
                'size': folder_size,
            })
        for file in file_names:
            if file == '.DS_Store':
                continue
            new_dict_list.append({
                'object_name': file,
                'parent_directory': dir_path,
                'object_type': 'file',
                'size': path.getsize(path.join(f'{dir_path}/{file}')),
            })
    print(new_dict_list)

    with open(file_json, 'w', encoding='utf-8') as j:
        json.dump(new_dict_list, j, indent=2)

    with open(file_csv, 'w', newline='', encoding='utf-8') as c:
        csv_writer = csv.DictWriter(c, fieldnames=(new_dict_list[0].keys()), dialect='excel-tab')
        csv_writer.writeheader()
        csv_writer.writerows(new_dict_list)

    with open(file_pickle, 'wb') as p:
        pickle.dump(new_dict_list, p, protocol=pickle.DEFAULT_PROTOCOL)


if __name__ == '__main__':
    inspect_dir(pathlib.Path.cwd())
