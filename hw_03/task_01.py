# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

new_list = [1, 1, 3, 4, 5, 6, 7, 5, 2, 4, 6, 7, 8, 9, 55, 56, 55]
new_list_dub = []
for el in new_list:
    if new_list.count(el) > 1:
        new_list_dub.append(el)
print(list(set(new_list_dub)))