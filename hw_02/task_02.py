# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение * дробей. Для проверки своего кода используйте модуль fractions.

import math
import fractions


def fr_sum(num_1, num_2):
    fr_1 = num_1.split('/')
    fr_2 = num_2.split('/')
    if int(fr_2[1]) != int(fr_1[1]):
        den_res = int(fr_2[1]) * int(fr_1[1])
        num_1_new = int(fr_1[0]) * int(fr_2[1])
        num_2_new = int(fr_2[0]) * int(fr_1[1])
        num_res = num_1_new + num_2_new
    com_div = math.gcd(num_res, den_res)
    if com_div > 1:
        num_res /= com_div
        den_res /= com_div
    print(f'Сумма дробей: {int(num_res)}/{int(den_res)}')
    f1 = fractions.Fraction(int(fr_1[0]), int(fr_1[1]))
    f2 = fractions.Fraction(int(fr_2[0]), int(fr_2[1]))
    print(f'Сумма с помощью fractions: {f1 + f2}')


def fr_mult(num_1, num_2):
    fr_1 = num_1.split('/')
    fr_2 = num_2.split('/')
    num_res = int(fr_1[0]) * int(fr_2[0])
    den_res = int(fr_1[1]) * int(fr_2[1])
    com_div = math.gcd(num_res, den_res)
    if com_div > 1:
        num_res /= com_div
        den_res /= com_div
    print(f'Произведение дробей: {int(num_res)}/{int(den_res)}')
    f1 = fractions.Fraction(int(fr_1[0]), int(fr_1[1]))
    f2 = fractions.Fraction(int(fr_2[0]), int(fr_2[1]))
    print(f'Произведение с помощью fractions: {f1 * f2}')


num_1 = input("Введите первую дробь в формате a/b: ")
num_2 = input("Введите вторую дробь в формате a/b: ")

fr_sum(num_1, num_2)
fr_mult(num_1, num_2)