"""Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""

from sys import argv

MIN_DATE = 1
MAX_YEAR = 9999
MAX_MONTH = 12
MAX_DAY = 31


def is_real_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if not (MIN_DATE <= year <= MAX_YEAR and MIN_DATE <= month <= MAX_MONTH and MIN_DATE <= day <= MAX_DAY):
        return False

    if month in (4, 6, 9, 11) and day > 30:
        return False

    if month == 2 and _is_leap(year) and day > 29:
        return False

    if month == 2 and not _is_leap(year) and day > 28:
        return False

    return True


def _is_leap(year: int) -> bool:
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))


if __name__ == '__main__':
    print(f'Введённая дата существует' if is_real_date(argv[1]) else 'Введённая дата невозможна')
