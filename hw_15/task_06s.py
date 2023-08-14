# Задание №6
# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
import logging
import os
from collections import namedtuple

logging.basicConfig(filename='task_06.log', filemode='w', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)

file = namedtuple(typename='file', field_names='name, ext, is_folder, parent_folder')


def parse():
    parser = argparse.ArgumentParser(prog='task_06 sem_15',
                                     epilog='inspect_dir',
                                     description='This module inspects directory')
    parser.add_argument('-p', '--path', default=os.getcwd(), help='Directory path')

    arg = parser.parse_args()
    return directory_info(arg.path)


def directory_info(file_p: str) -> None:
    files_list = os.walk(file_p)
    for dir_path, dir_names, file_names in files_list:
        for folder in dir_names:
            obj = file(folder, None, True, dir_path.split('/')[-1])
            logger.info(obj)
        for f in file_names:
            file_name, file_ext = f.split('.')
            obj = file(file_name, file_ext, False, dir_path.split('/')[-1])
            logger.info(obj)


if __name__ == '__main__':
    parse()
    # python3 task_06.py -p 'folder path'
