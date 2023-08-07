
# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.

import csv


class IsCapitalised:
    """Проверка слова на первую заглавную букву и наличие только букв"""

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    @staticmethod
    def validate(value):
        """Проверка слова на наличие только букв и первую заглавную букву"""
        if not value.isalpha():
            raise TypeError(f'ФИО должны состоять только из букв!')
        if not value.istitle():
            raise ValueError(f'Первая буква ФИО должна быть заглавной!')


class NumberRange:
    """Проверка вхождения числа в диапазон"""

    def __init__(self, min_num: int = None, max_num: int = None):
        self._min_num = min_num
        self._max_num = max_num

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        """Проверка вхождения числа в диапазон"""
        if not isinstance(value, int):
            raise TypeError(f'{value} должно быть целым числом')
        if self._min_num is not None and value < self._min_num or self._max_num is not None and value > self._max_num:
            raise ValueError(f'{value} должно находиться в диапазоне от {self._min_num} до {self._max_num}')


class Student:
    """Класс студента, хранящий ФИО, предметы, оценки и результаты тестов.\n
    Экземпляр класса сообщает средний балл по тестам для каждого предмета
    и по оценкам всех предметов вместе взятых."""
    _last_name = IsCapitalised()
    _name = IsCapitalised()
    _patronymic = IsCapitalised()
    _grades = NumberRange(2, 5)
    _test_results = NumberRange(0, 100)

    def __init__(self, last_name: str, name: str, patronymic: str, file_name: str):
        self._last_name = last_name
        self._name = name
        self._patronymic = patronymic
        self._file_name = file_name
        self._subjects = self._subjects_from_scv()

    def __repr__(self):
        return f"Student('{self._last_name}', '{self._name}', '{self._patronymic}', '{self._file_name}')"

    @property
    def full_name(self):
        return f'{self._last_name} {self._name} {self._patronymic}'

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, value):
        if len(value) == 3:
            if value[0].capitalize() in self._subjects.keys():
                subj, grades, test_results = value
                if isinstance(grades, int):
                    self._grades = grades
                else:
                    for item in grades:
                        self._grades = item

                if isinstance(test_results, int):
                    self._test_results = test_results
                else:
                    for item in test_results:
                        self._test_results = item

                self._subjects.update({subj.capitalize():
                                       {'Оценки': grades if isinstance(grades, list)
                                        else [grades],
                                        'Результаты тестов': test_results if isinstance(test_results, list)
                                        else [test_results]}})
            else:
                print(f'Предмета {value[0]} нет у данного студента!')
        else:
            print('Неверное количество аргументов!')

    def _subjects_from_scv(self):
        """Метод, возвращающий словарь предметов из файла *.csv"""
        with open(self._file_name, encoding='utf-8') as file:
            csv_data = csv.DictReader(file, dialect='excel-tab', lineterminator='\n')
            subjects_list = [subject[0] for subject in csv_data.reader][1:]
            results = {subject: {'Оценки': [], 'Результаты тестов': []} for subject in subjects_list}
        return results

    def print_grade(self):
        """Метод печати общей успеваемости студента"""
        print(f'Успеваемость студента {self.full_name}:')
        for item in self._subjects.items():
            print(item)
        print()

    def __str__(self):
        """Информация о студенте, средний балл по оценкам и тестам для каждого предмета"""
        res = {}
        for key, items in self._subjects.items():
            res.update({key: f'{sum(items.get("Оценки")) / len(items.get("Оценки"))} / '
                             f'{sum(items.get("Результаты тестов")) / len(items.get("Результаты тестов"))}'})
        strings = []
        for key, item in res.items():
            strings.append("{}: {}".format(key.capitalize(), item))
        result = "; ".join(strings)
        return f'Студент "{self.full_name}"\n' \
               f'Средний балл по предметам (оценки / тесты):\n' \
               f'{result}'


if __name__ == '__main__':
    new_student = Student('Иванов', 'Иван', 'Иванович', 'subjects.csv')
    new_student.subjects = 'Русский язык', 2, 30
    new_student.subjects = 'Математика', [5, 4, 3, 5, 5], [90, 86, 66, 80]
    new_student.subjects = 'Физика', [4, 4, 4, 5, 3], [70, 84, 90, 77]
    new_student.subjects = 'Химия', [3, 3, 3, 4, 4], [50, 30, 69, 70]
    new_student.subjects = 'Английский язык', 2, 50
    new_student.print_grade()
    print(new_student)
