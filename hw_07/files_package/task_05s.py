"""Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи"""

from random import choices, randint
from string import ascii_lowercase, digits


def gen_ext_(ext: str, name_len_min: int = 6, name_len_max: int = 30, bytes_min: int = 256, bytes_max: int = 4096,
            num_files: int = 42) -> None:
    for _ in range(num_files):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(name_len_min, name_len_max)))
        data = bytes(randint(0, 255) for _ in range(randint(bytes_min, bytes_max)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)


def gen_more_ext(**extensions) -> None:
    for extension, num in extensions.items():
        gen_ext_(ext=extension, num_files=num)


if __name__ == '__main__':
    gen_more_ext(txt=2, rtf=1, bmp=1)
