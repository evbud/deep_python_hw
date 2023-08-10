# Задание №6
# На семинаре l13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import json
import pytest

from folder.t4 import UserData
from folder.t5 import Project
from folder.t6 import MyLevelEx, MyAccessEx

JSON_FILE = 'task_06s.json'


@pytest.fixture
def users_data():
    data = {
        UserData('John', 101, 1),
        UserData('Vasya', 102, 3),
        UserData('Petya', 103, 3),
        UserData('Mike', 104, 6),
    }
    return data


@pytest.fixture
def high_level_user():
    return UserData('John', 101, 1)


@pytest.fixture
def new_low_level_user():
    return UserData('Paul', 105, 5)


def test_load_json(users_data):
    """Тестирование загрузки данных из JSON файла"""
    data = {
        1: {101: 'John'},
        3: {102: 'Vasya', 103: 'Petya'},
        6: {104: 'Mike'}
    }
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    project1 = Project()
    test_result = project1.load_json(JSON_FILE)
    assert test_result == users_data


def test_enter_valid_user(high_level_user):
    """Вход в систему существующего пользователя"""
    new_project = Project()
    new_project.load_json(JSON_FILE)
    test_user = new_project.enter('John', 101)
    assert test_user == high_level_user


def test_enter_invalid_user():
    """Вход в систему несуществующего пользователя"""
    new_project = Project()
    new_project.load_json(JSON_FILE)
    with pytest.raises(MyAccessEx, match=r'Пользователя с именем Johnny и id 101 нет в системе! Доступ запрещён!'):
        new_project.enter('Johnny', 101)


def test_add_lower_level_user(new_low_level_user):
    """Добавление пользователя с более низким уровнем, чем у администратора"""
    new_project = Project()
    new_project.load_json(JSON_FILE)
    new_project.enter('John', 101)
    new_user = new_project.add_user('Paul', 105, 5)
    assert new_user == new_low_level_user


def test_add_higher_level_user():
    """Добавление пользователя с более высоким уровнем, чем у администратора"""
    new_project = Project()
    new_project.load_json(JSON_FILE)
    new_project.enter('Mike', 104)
    with pytest.raises(MyLevelEx, match=r'Уровень доступа пользователя Bob - 1'
                                        r' ниже уровня доступа администратора 6!\n Доступ запрещён!'):
        new_project.add_user('Bob', 105, 1)


if __name__ == '__main__':
    pytest.main(['-v'])
