"""Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов."""

import json
import pickle
from pathlib import Path


def json_to_pickle(path: str) -> None:
    directory = Path(path)
    files = [files for files in directory.iterdir() if files.suffix == '.json']
    for file in files:
        with open(file, 'r', encoding='utf-8') as j:
            data = json.load(j)
        with open(f'{directory}/{file.stem}.pickle', 'wb') as p:
            pickle.dump(data, p)


if __name__ == '__main__':
    json_to_pickle(Path().cwd())
