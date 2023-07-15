"""Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться."""

import json
import os


def add_user(data_file: str) -> None:
    tmp_set = set()
    if os.path.isfile(data_file):
        with open(data_file, 'r', encoding='utf-8') as f:
            new_dict = json.load(f)
        for _, value in new_dict.items():
            tmp_set.update(value.keys())
    else:
        new_dict = {str(i): {} for i in range(1, 8)}
    while True:
        name, id_num, level = input('Введите через пробел имя, id, уровень доступа от 1 до 7 : ').split()
        if id_num in tmp_set and new_dict[level].get(id_num) is None:
            continue
        tmp_set.update(id_num)
        new_dict[level].update({id_num: name})
        with open(data_file, 'w+', encoding='utf-8') as j:
            json.dump(new_dict, j, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    add_user('task_02.json')
