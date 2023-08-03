# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.


class Archive:
    """Класс Архив, который хранит пару свойст.
При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра"""

    __instance = None

    def __init__(self, num: int, text: str):
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance

    def __str__(self):
        return f'Text: {self.text}, number: {self.num}, txt archive: {self.text_list}, num archive: {self.num_list}'

    def __repr__(self):
        return f'Text: {self.text}, number: {self.num}'


if __name__ == '__main__':
    new_arch = Archive(1, 'test')
    new_arch_1 = Archive(2, 'test_1')

    print(new_arch_1)
    print(f'{new_arch_1 = }')
    print(repr(new_arch_1))

    print(help(new_arch_1))
