"""Задание №6
Доработайте классы исключения так, чтобы они выдали
подробную информацию об ошибках.
Передавайте необходимые данные из основного кода
проекта."""


class MyExClass(Exception):
    pass


class MyLevelEx(MyExClass):
    def __init__(self, user_name: str, user_level: int, admin_level: int):
        self.user_level = user_level
        self.user_name = user_name
        self.admin_level = admin_level

    def __str__(self):
        return f'Уровень доступа пользователя {self.user_name} - {self.user_level} ' \
               f'ниже уровня доступа администратора {self.admin_level}!\n Доступ запрещён!!'


class MyAccessEx(MyExClass):
    def __init__(self, user_id: int, user_name: str):
        self.user_id = user_id
        self.user_name = user_name

    def __str__(self):
        return f'Пользователя с именем {self.user_name} и id {self.user_id} нет в системе! Доступ запрещён!'


if __name__ == '__main__':
    lvl1 = 5
    lvl2 = 9
    if lvl2 > 6:
        print('Ok!')
    else:
        raise MyLevelEx(lvl2)

    if lvl1 > 6:
        print('Ok!')
    else:
        raise MyLevelEx(lvl1)
