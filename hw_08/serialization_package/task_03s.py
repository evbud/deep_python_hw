"""Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV."""

import csv
import json


def json_to_csv(file_json: str, file_csv: str) -> None:
    with open(file_json, 'r', encoding='utf-8') as j:
        new_dict = json.load(j)
        new_list = []
        for level, value in new_dict.items():
            for id_num, name in value.items():
                new_list.append({
                    'level': int(level),
                    'id': int(id_num),
                    'name': name,
                })
    print(new_list)
    with open(file_csv, 'w', newline='', encoding='utf-8') as c:
        csv_writer = csv.DictWriter(c, fieldnames=(new_list[0].keys()), dialect='excel-tab')
        csv_writer.writeheader()
        csv_writer.writerows(new_list)


if __name__ == '__main__':
    json_to_csv('task_02.json', 'task_03.csv')
