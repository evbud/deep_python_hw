# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def replacement_with_s(*word):
    word = list(word)
    words_without_s = []
    for i in range(len(word)):
        if word[i].endswith('s') and len(word[i]) > 1:
            words_without_s.append(word[i][:-1])
            word[i] = None
    return word, words_without_s


if __name__ == '__main__':
    print(replacement_with_s('actors', 'print', 'merinos', 's', 'parent'))
