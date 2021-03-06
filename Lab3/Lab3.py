# C3 == 2 "String"
# C17 == 15 "В заданому тексті замінити слова заданої довжини визначеним рядком."
# Створити клас, який складається з виконавчого методу, що виконує дію текстовим рядком (п.3), тип якого визначено варіантом (п.2).
# Необхідно обробити всі виключні ситуації, що можуть виникнути під час виконання програмного коду.
# Всі змінні повинні бути описані та значення їх задані у виконавчому методі.

import re


class Main():
    def __init__(self):
        text = "Створити клас, який складається з виконавчого методу, що виконує дію текстовим рядком, тип якого визначено варіантом.\
Необхідно обробити всі виключні ситуації, що можуть виникнути під час виконання програмного коду.\
Всі змінні повинні бути описані та значення їх задані у виконавчому методі."
        if type(text) is not str:
            print("Заміняти слова треба в тексті, написано ж")
            return
        replace = str(input("Введіть, чим ви хочете замінити слова: "))
        try:
            word_length = int(input("Введіть довжину слів, які треба замінити: "))
        except ValueError:
            print("Довжина шуканих слів повинна бути цілим числом, це ж очевидно, блін")
            return

        text = re.sub("\\b[а-яА-Яa-zA-Z]{"+str(word_length)+"}\\b", replace, text)
        print(text)


main = Main()

