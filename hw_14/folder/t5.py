"""Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа."""

from .t4 import UserData, data_from_json
from .t6 import MyLevelEx, MyAccessEx


class Project:
    def __init__(self):
        self._current_user = None
        self._users = set()

    def load_json(self, path: str) -> set:
        self._users = data_from_json(path)
        return self._users

    def enter(self, name: str, user_id: int) -> UserData:
        test_user = UserData(name, user_id, 0)
        if test_user not in self._users:
            raise MyAccessEx(user_id, name)
        for item in self._users:
            if item == test_user:
                self._current_user = item
                return self._current_user

    def add_user(self, name: str, user_id: int, level: int) -> UserData:
        if level < self._current_user.level:
            raise MyLevelEx(name, level, self._current_user.level)

        new_user = UserData(name, user_id, level)
        self._users.add(new_user)
        return new_user

#
# if __name__ == '__main__':
#     pj1 = Project()
#     pj1.load_json('task_04.json')
#     print(pj1.enter('Test', 10))
#     # print(pj1.enter('Tellst', l10))
#     print(f'Добавлен {pj1.add_user("Test1", 987, 9)}')
#     # print(f'Добавлен {pj1.add_user("New", 565, 1)}')
#     print(pj1.enter('Test1', 987))
