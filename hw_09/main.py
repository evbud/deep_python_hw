import games_package

if __name__ == '__main__':
    task_num = int(input(f'Введите номер задачи для демонстрации:\n'
                         f'1 - Игра угадай число\n'
                         f'2 - Загадки\n'))

    match task_num:
        case 1:
            game = games_package.guess_number(0, 0)
            print(game)
        case 2:
            quest_dict = {'Зимой и летом одним цветом': ['елка', 'ёлка', 'ель', 'елочка', 'ёлочка', 'сосна'],
                          'Не лает, не кусает, а в дом не пускает': ['замок', 'замочек'],
                          'Сидит дед, во сто шуб одет': ['лук', 'луковица'],
                          'Висит груша - нельзя скушать': ['лампа', 'лампочка']}
            games_package.questions_dict(quest_dict)

