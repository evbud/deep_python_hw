"""Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки."""

import json


def txt_to_json(file: str) -> None:
    new_json_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            new_json_dict[name.capitalize()] = float(number)
    print(new_json_dict)
    with open('task_01.json', 'w', encoding='utf-8') as j:
        json.dump(new_json_dict, j, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    txt_to_json('task_01_example.txt')
