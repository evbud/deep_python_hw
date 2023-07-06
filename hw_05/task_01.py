"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""

import os


def split_abs_path(abs_link: str) -> tuple:
    full_path, file_name_with_ext = os.path.split(abs_link)
    file_name, extension = str(file_name_with_ext).split('.')
    return full_path, file_name, extension


if __name__ == '__main__':
    link = '/Users/username/Desktop/python/project.py'
    print(split_abs_path(link))
    print(split_abs_path(__file__))
