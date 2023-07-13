"""Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён."""

import os.path
from random import choices, randint
from string import ascii_lowercase, digits


def gen_ext_upd(ext: str, name_len_min: int = 6, name_len_max: int = 30, bytes_min: int = 256, bytes_max: int = 4096,
                num_files: int = 42, folder_name: str = 'files') -> None:
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    for _ in range(num_files):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(name_len_min, name_len_max)))
        data = bytes(randint(0, 255) for _ in range(randint(bytes_min, bytes_max)))
        file_name = f'{name}.{ext}'
        if file_name not in os.listdir(folder_name):
            with open(f'{folder_name}/{file_name}', 'wb') as f:
                f.write(data)
        else:
            print(f'Файл {file_name} уже существует и не был записан!')


def gen_more_ext_upd(**extensions) -> None:
    for extension, num in extensions.items():
        gen_ext_upd(ext=extension, num_files=num)


if __name__ == '__main__':
    gen_more_ext_upd(txt=3, bmp=1, mp3=2, mkv=1, dmg=1)
