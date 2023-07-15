from pathlib import Path
import serialization_package

if __name__ == '__main__':
    task_num = int(input(f'Введите номер задачи для демонстрации:\n'
                         f'1 - Создание JSON из ранее созданного текстового файла\n'
                         f'2 - Создание/дополнение JSON-файла данными о пользователях\n'
                         f'3 - Сохранение ранее созданного JSON в CSV\n'
                         f'4 - Построчное преобразование данных из ранее созданного CSV и сохранение в JSON\n'
                         f'5 - Сохранение JSON файлов заданной директории в одноименные PICKLE-файлы\n'
                         f'6 - Сохранение ранее созданного в задаче 4 PICKLE-файла в CSV\n'
                         f'7 - Печать в консоль созданного в задаче 6 CSV-файла как PICLE строки\n'
                         f'8 - Рекурсивный обход указанной директории и сохранение результатов в файлы\n'))

    match task_num:
        case 1:
            serialization_package.txt_to_json('serialization_package/task_01_example.txt')
        case 2:
            serialization_package.add_user('task_02.json')
        case 3:
            serialization_package.json_to_csv('task_02.json', 'task_03.csv')
        case 4:
            serialization_package.csv_to_json('task_03.csv', 'task_04.json')
        case 5:
            serialization_package.json_to_pickle(Path().cwd())
        case 6:
            serialization_package.pickle_to_csv('task_04.pickle', 'task_06.csv')
        case 7:
            serialization_package.print_pickle_from_csv('task_06.csv')
            serialization_package.print_pickle_from_csv_rl('task_06.csv')
        case 8:
            serialization_package.inspect_dir(Path().cwd())
