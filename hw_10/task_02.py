"""Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов экземпляра."""

from os import listdir, mkdir, makedirs, path, rename
from random import choices, randint
from string import ascii_lowercase, digits


class Files:
    def __init__(self, ext: str = 'txt', folder: str = 'files', name_len_min: int = 6, name_len_max: int = 30,
                 bytes_min: int = 256, bytes_max: int = 4096, num_files: int = 3):
        self.folder = folder
        self.ext = ext
        self.name_len_min = name_len_min
        self.name_len_max = name_len_max
        self.bytes_min = bytes_min
        self.bytes_max = bytes_max
        self.num_files = num_files

    def gen_files(self) -> None:
        """функция генерирует файлы с разными расширениями.
        Расширения и количество файлов функция принимает в качестве параметров.
        Количество переданных расширений может быть любым."""

        if not path.exists(self.folder):
            mkdir(self.folder)
        for _ in range(self.num_files):
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(self.name_len_min, self.name_len_max)))
            data = bytes(randint(0, 255) for _ in range(randint(self.bytes_min, self.bytes_max)))
            file_name = f'{name}.{self.ext}'
            if file_name not in listdir(self.folder):
                with open(f'{self.folder}/{file_name}', 'wb') as f:
                    f.write(data)
            else:
                print(f'Файл {file_name} уже существует и не был записан!')

    def sort_files(self) -> None:
        """функция для сортировки файлов по директориям: видео, изображения, текст и т.п.
        Каждая группа включает файлы с несколькими расширениями.
        В исходной папке остаются только те файлы, которые не подошли для сортировки."""

        ext_dict = {'video': ['avi', 'mkv', 'mp4'],
                    'audio': ['wav', 'mp3'],
                    'text': ['txt', 'doc', 'rtf', 'pdf'],
                    'image': ['bmp', 'gif', 'jpg', 'jpeg', 'png'],
                    'binary': ['bin'],
                    }
        files = listdir(self.folder)

        for file in files:
            for file_type, ext in ext_dict.items():
                if file.split('.')[-1].lower() in ext:
                    makedirs(f'{self.folder}/{file_type}', exist_ok=True)
                    rename(f'{self.folder}/{file}', f'{self.folder}/{file_type}/{file}')


if __name__ == '__main__':
    new_files = {'txt': 3, 'bmp': 2}
    for extension, num in new_files.items():
        make_files = Files(ext=extension, num_files=num)
        make_files.gen_files()
        make_files.sort_files()
