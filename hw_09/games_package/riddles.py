# Функция questions_dict() принимает на вход строку (текст загадки) и
# число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря
# в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

_result = {}


def guessing(text: str, variants: list[str], tries: int) -> int:
    print(f'Отгадайте загадку:\n{text}')

    for count in range(1, tries + 1):
        answer = input(f'Попытка №{count}... введите отгадку: ')
        if answer.lower() in variants:
            print(f'Вы угадали!\n')
            return count

    print(f'Вы не угадали...\n')
    return 0


def questions_dict(q_dict: dict[str: list[str]], count: int = 3) -> None:
    for key, value in q_dict.items():
        res = guessing(key, value, count)
        result_score(key, res)
        # print(f'\nCode {res}')

    print_stat()


def result_score(txt: str, tries: int) -> None:
    _result.update({txt: tries})


def print_stat():
    res = (f'Загадка "{key}" отгадана, потрачено попыток: {value}' if value > 0 else f'Загадка не отгадана'
           for key, value in _result.items())
    print('Статистика: ')
    print('\n'.join(res))


if __name__ == '__main__':
    quest_dict = {'Зимой и летом одним цветом': ['елка', 'ёлка', 'ель', 'елочка', 'ёлочка', 'сосна'],
                  'Не лает, не кусает, а в дом не пускает': ['замок', 'замочек'],
                  'Сидит дед, во сто шуб одет': ['лук', 'луковица'],
                  'Висит груша - нельзя скушать': ['лампа', 'лампочка']}

    questions_dict(quest_dict)
