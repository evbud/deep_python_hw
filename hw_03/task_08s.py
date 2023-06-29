# ✔ Три друга взяли вещи в поход.
# Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

hike = {'Вася': ['рюкзак', 'спальник', 'дождевик', 'спички', 'палатка', 'навигатор', 'нож', 'аптечка'],
        'Петя': ['рюкзак', 'спальник', 'дождевик', 'спички', 'палатка', 'соль', 'вода'],
        'Саша': ['рюкзак', 'спальник', 'дождевик', 'навигатор', 'соль', 'тушенка', 'макароны'],
        }

every_friend_stuff = set()

for key, value in hike.items():
    every_friend_stuff.update(value)
    intersect_stuff = set(value)
    diff_stuff = set(value)
    for key_tmp, value_tmp in hike.items():
        intersect_stuff &= intersect_stuff.intersection(value_tmp)
        if key != key_tmp:
            diff_stuff -= set(value_tmp)

    print(f'Список уникальных вещей, которые взял только {key}:', ', '.join(diff_stuff))

print(f'Список вещей всех друзей(без повторов):', ', '.join(every_friend_stuff))
print(f'Каждый друг взял:', ', '.join(intersect_stuff))

for key, value in hike.items():
    intersect_but_diff = set()
    count = 1
    for key_tmp, value_tmp in hike.items():
        if key != key_tmp:
            if count == 1:
                intersect_but_diff = set(value_tmp)
            else:
                intersect_but_diff &= set(value_tmp)
            count += 1
    for item in intersect_but_diff:
        if item not in value:
            print(f'У друга "{key}" нет "{item}", но есть у остальных друзей')