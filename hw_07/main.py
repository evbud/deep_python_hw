import files_package

if __name__ == '__main__':
    task_num = int(input(f'Введите номер задачи для демонстрации:\n'
                         f'1 - Заполнение файла случайными парами чисел int | float\n'
                         f'2 - Генерация случайных псевдоимён и сохранение их в файл\n'
                         f'3 - Сохранение в файл имён и произведений пар чисел из созданных в 1-2 задачах файлов\n'
                         f'4 - Создание файлов с указанным расширением\n'
                         f'5 - Создание заданного количества файлов указанных расширений\n'
                         f'6 - Создание заданного количества файлов указанных расширений в указанную директорию\n'
                         f'7 - Сортировка файлов по директориям\n'
                         f'8 - Групповое переименование файлов\n'))

    match task_num:
        case 1:
            files_package.rand_pares(3, 'task_01s.txt')
        case 2:
            files_package.pseudo_gen(10, 'task_02s.txt')
        case 3:
            files_package.convert('task_02s.txt', 'task_01s.txt', 'task_03s.txt')
        case 4:
            files_package.gen_ext('txt')
        case 5:
            files_package.gen_more_ext(txt=2, rtf=1, bmp=1)
        case 6:
            files_package.gen_more_ext_upd(txt=3, bmp=1, mp3=2, mkv=1, dmg=1)
        case 7:
            files_package.sort_files('files')
        case 8:
            files_package.rename_files(2, 'txt', 'rtf', [1, 3], '_test')
