# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def input_n():
    system: int = 0
    while system not in (2, 8, 16):
        system = int(input(f'В какую систему счисления первести число?\n'
                           f'Двоичная - введите "2"\n'
                           f'Восьмеричная - введите "8"\n'
                           f'Шестнадцатиричная - введите "16"'))
    return system


def dec_to_n(number: int, system: int) -> str:
    hex_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    tmp_num = number
    new_num: str = ''
    while tmp_num != 0:
        mod: str = str(tmp_num % system)
        for el in hex_dict:
            if mod.isdigit() and int(mod) == int(el):
                mod = hex_dict.get(el)
        new_num = mod + new_num
        tmp_num //= system
    return new_num


if __name__ == '__main__':
    num = int(input('Введите целое число: '))
    nn: str = dec_to_n(num, input_n())
    print(nn)
    print(f'Это число в двоичном представлении - {bin(num)}')
    print(f'Это число в восьмеричном представлении - {oct(num)}')
    print(f'Это число в шестнадцатеричном представлении - {hex(num)}')