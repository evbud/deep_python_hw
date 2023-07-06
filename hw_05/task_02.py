"""Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""


def bonus_gen(names: list[str], salary: list[int], bonus: list[str]) -> dict[str: float]:
    bonus_dict = {names[i]: (float(salary[i]) * float(bonus[i][:-1:])) / 100 for i in range(len(names))
                  if len(names) == len(salary) == len(bonus)}
    return bonus_dict


if __name__ == '__main__':
    name_list = ['Иванов', 'Петров', 'Сидоров']
    salary_list = [85000, 95000, 100000]
    bonus_list = ['10.25%', '15.25%', '17.25%']

    print(bonus_gen(name_list, salary_list, bonus_list))