"""Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""

from os import listdir, makedirs, rename


def sort_files(folder: str) -> None:
    ext_dict = {'video': ['avi', 'mkv', 'mp4'],
                'audio': ['wav', 'mp3'],
                'text': ['txt', 'doc', 'rtf', 'pdf'],
                'image': ['bmp', 'gif', 'jpg', 'jpeg', 'png'],
                'binary': ['bin'],
                }
    files = listdir(folder)

    for file in files:
        for file_type, ext in ext_dict.items():
            if file.split('.')[-1].lower() in ext:
                makedirs(f'{folder}/{file_type}', exist_ok=True)
                rename(f'{folder}/{file}', f'{folder}/{file_type}/{file}')


if __name__ == '__main__':
    sort_files('files')
