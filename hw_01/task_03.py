# ✔ Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1001

num = randint(LOWER_LIMIT, UPPER_LIMIT)
TRIES_MAX = 10

tries_count = 0
num_try = 0

while num_try != num and tries_count < TRIES_MAX:
    num_try = int(input("Угадайте число: "))
    if (num_try < num):
        tries_count += 1
        print(f'Больше! осталось {TRIES_MAX - tries_count} попыток')
        if tries_count == TRIES_MAX:
            print(f"Потрачено! Вы не угадали! Число {num}")
    elif (num_try > num):
        tries_count += 1
        print(f'Меньше! осталось {TRIES_MAX - tries_count} попыток')
        if tries_count == TRIES_MAX:
            print(f"Потрачено! Вы не угадали! Число {num}")
    elif num_try == num:
        print(f"Поздравляем! Вы угадали! Число {num}")