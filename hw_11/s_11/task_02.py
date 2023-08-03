# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра


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


if __name__ == '__main__':
    new_arch = Archive(1, 'test')
    print(new_arch.num_list)
    print(new_arch.text_list)

    new_arch_1 = Archive(2, 'Hello')
    print(new_arch_1.num_list)
    print(new_arch_1.text_list)

    new_arch_2 = Archive(3, "world!")
    print(new_arch_2.num_list)
    print(new_arch_2.text_list)

    print(new_arch_2.__doc__)
