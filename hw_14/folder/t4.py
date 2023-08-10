"""Задание №4
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей."""

import json


class UserData:
    def __init__(self, name: str, user_id: int, level: int):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'{self.name}, id: {self.user_id}, level: {self.level}'

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self):
        return hash((self.name, self.user_id))


def data_from_json(file_name: str) -> set[UserData]:
    with open(file_name, encoding='utf-8') as j:
        users_dict = json.load(j)
    users = set()
    for level, user_data in users_dict.items():
        for user_id, name in user_data.items():
            users.add(UserData(name, int(user_id), int(level)))
    return users

#
# if __name__ == '__main__':
#     users_set = data_from_json('task_04.json')
#     for user in users_set:
#         print(user)
