# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

MULTI = 50
PERCENT = 0.085
EXTRA_PERCENT = 0.97
RICH_PERCENT = 0.1
MIN_CASH = 30
MAX_CASH = 600
MAX_COUNT = 3
MAX_SCORE = 5_000_000
count = 0
total_score = 0


def add_cash(cash):
    global total_score
    global count
    temp_cash = cash
    rich_tax(temp_cash)
    while temp_cash % MULTI != 0 or temp_cash <= 0:
        temp_cash = int(input("Некорректная сумма!\nВведите сумму пополнения кратную 50: "))
        rich_tax(temp_cash)
    if count % MAX_COUNT == 0 and count > 0:
        temp_cash *= EXTRA_PERCENT
    count += 1
    total_score += temp_cash
    return total_score


def give_cash(cash):
    global total_score
    global count
    temp_cash = cash
    rich_tax(temp_cash)
    while temp_cash % MULTI != 0 or temp_cash <= 0:
        temp_cash = int(input("Некорректная сумма!\nВведите сумму снятия кратную 50: "))
        rich_tax(temp_cash)
    while temp_cash > total_score:
        temp_cash = int(input("Недостаточно средств!\nВведите сумму снятия кратную 50: "))
        rich_tax(temp_cash)
    percent_temp = temp_cash * PERCENT
    if percent_temp < MIN_CASH:
        percent_temp = MIN_CASH
    elif percent_temp > MAX_CASH:
        percent_temp = MAX_CASH
    if count % MAX_COUNT == 0 and count > 0:
        temp_cash *= EXTRA_PERCENT
    count += 1
    total_score -= temp_cash
    total_score -= percent_temp
    return total_score


def rich_tax(temp_cash):
    global total_score
    if total_score > MAX_SCORE:
        rich_rate = temp_cash * RICH_PERCENT
        total_score -= rich_rate


def main_menu():
    selector = 0
    while selector not in (1, 2, 3, 4):
        selector = int(input("Выберите действие:\n"
                             "1. Показать баланс\n"
                             "2. Пополнить\n"
                             "3. Снять\n"
                             "4. Выход\n"))
    match selector:
        case 1:
            print(total_score)
            main_menu()
        case 2:
            add_cash(int(input("Введите сумму пополнения кратную 50: ")))
            main_menu()
        case 3:
            give_cash(int(input("Введите сумму снятия кратную 50: ")))
            main_menu()
        case 4:
            quit()


main_menu()