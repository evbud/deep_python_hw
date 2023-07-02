# ✔ Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем (хешируемы только неизменяемые типы данных),
# используйте его строковое представление.


def dict_func(**kwargs):
    new_dict = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, set, bytearray, dict)):
            value = str(value)
        new_dict[value] = key
    return new_dict


if __name__ == '__main__':
    print(dict_func(cat='Vasiliy', cat_age=10, cat_toys=['mouse', 'laser', 'snake'],
                    cat_food_daily={'dry': 70, 'water': 300}, cat_locations={'bed', 'floor', 'bath', 'windowsill'}))
