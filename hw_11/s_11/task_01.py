# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

from time import time


class MyString(str):
    """Класс 'Моя Строка', где:
- доступны все возможности str
- дополнительно хранятся имя автора строки и время создания"""

    def __new__(cls, value: str, author_name: str):
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.time_created = time()
        print(f'class {cls} created')
        return instance


if __name__ == '__main__':
    new_str = MyString('Hello world!', 'Johnny')
    print(new_str.author_name)
    print(new_str.time_created)

    print(MyString.__doc__)
    print(new_str.__doc__)
