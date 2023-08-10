"""Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции."""

import json
import csv


def csv_to_json(file_csv: str, file_json: str) -> None:
    with open(file_csv, 'r', encoding='utf-8') as f:
        csv_file = csv.reader(f, delimiter='\t')
        dict_list = []
        for i, (level, user_id, user_name) in enumerate(csv_file):
            if i:
                dict_list.append({
                    'level': level,
                    'ID': user_id.zfill(10),
                    'name': user_name,
                    'hash': hash(user_id + user_name)
                })
        print(dict_list)

    with open(file_json, 'w', encoding='utf-8') as j:
        json.dump(dict_list, j, indent=2)


if __name__ == '__main__':
    csv_to_json('task_03.csv', 't4.json')
