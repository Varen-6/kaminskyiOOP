#  Модифікувати лабораторну роботу №3 наступним чином: для літер, слів, речень, розділових знаків та тексту створити окремі класи.
#  Слово повинно складатися з масиву літер, речення з масиву слів та розділових знаків, текст з масиву речень.
#  Замінити послідовність табуляцій та пробілів одним пробілом.

#  Створити клас, який складається з виконавчого методу, що виконує описану дію з лабораторної роботи №3, але в якості типів використовує створені класи.
#  Необхідно обробити всі виключні ситуації, що можуть виникнути під час виконання програмного коду.
#  Всі змінні повинні бути описані та значення їх задані у виконавчому методі.


class Main:
    def __init__(self):
        text = "Створити клас, який складається з виконавчого методу, що виконує дію текстовим рядком, тип якого визначено варіантом. \
Необхідно обробити всі виключні ситуації, що можуть виникнути під час виконання програмного коду. \
Всі змінні повинні бути описані та значення їх задані у виконавчому методі. \
Лабораторні роботи прохання надсилати електронною поштою. \
Лабораторна робота №5 - це бонусна лабораторна робота для студентів, які не писали Coursera. \
При виявленні плагіату оцінка знижується всім, хто в цьому бере участь. \
Сертифікати приймаю тільки у вигдяді посилань на сайт Courserа з відсотками. \
Переписування прохання більше не надсилати. \
Приймаю тільки нові сертифікати. \
Бали за Courserа будуть зараховуватися тільки за умови здачі ВСІХ лабораторних робіт. "

        while True:
            try:
                replace_len = int(input("Введіть довжину слів, які потрібно заміняти:"))
                break
            except TypeError:
                pass
        replace_with = Word(str(input("Введіть, чим будемо заміняти:")))
        obj_text = Text(text)
        print(obj_text.str())
        for i in range(len(obj_text.sentences)):
            for j in range(len(obj_text.sentences[i].content)):
                if obj_text.sentences[i].content[j].type() == "Word":
                    if obj_text.sentences[i].content[j].length() == replace_len:
                        obj_text.sentences[i].content[j] = replace_with
        print(obj_text.str())


class Text:  # Класс текстів
    def __init__(self, text):
        self.text = text.split(". ")
        self.sentences = []
        for e in range(len(self.text)):
            if self.text[e] != "":
                self.sentences.append(Sentence(self.text[e]))

    def type(self):  # Функція, що відображ. тип
        return "Text"

    def str(self):  # Функція отримання str тексту
        return "".join([sentence.get_sentence() for sentence in self.sentences])


class Sentence:  # Клас речення
    def __init__(self, text):
        self.sentence = text.split(" ")
        self.content = []
        for i in range(len(self.sentence)):
            if self.sentence[i] == "-":
                self.content.append(PuncSymbol(self.sentence[i]))
            elif self.sentence[i] == "":
                pass
            elif self.sentence[i][-1] == "," or self.sentence[i][-1] == ":" or self.sentence[i][-1] == ";":
                self.content.extend([Word(self.sentence[i][:-1]), PuncSymbol(self.sentence[i][-1])])
            elif self.sentence[i] == self.sentence[-1]:
                self.content.extend([Word(self.sentence[i]), PuncSymbol(".")])
            else:
                self.content.append(Word(self.sentence[i]))

    def type(self):  # Функція, що відображ. тип
        return "Sentence"

    def get_sentence(self):  # Функція отримання str речення
        sentence = []
        for i in range(len(self.content)):
            if self.content[i].get() == ".":
                sentence.extend([".", " "])
            elif self.content[i+1].type() != "PuncSymbol" or self.content[i+1].get() == "-":
                sentence.extend([self.content[i].get(), " "])
            else:
                sentence.append(self.content[i].get())
        return "".join(sentence)


class Word:  # Клас слів
    def __init__(self, text):
        self.letters = [Letter(text[i]) for i in range(len(text))]  # Створення масиву об. класу букв

    def type(self):  # Функція, що відображ. тип
        return "Word"

    def length(self):  # Функція для добування довжини слова
        return len(self.letters)

    def get(self):  # Функція переводу слова у str
        return "".join([letter.letter for letter in self.letters])


class Letter:  # Клас букв
    def __init__(self, letter):
        self.letter = letter

    def type(self):  # Функція, що відображ. тип
        return "Letter"


class PuncSymbol:  # Клас пунктуаційного символа
    def __init__(self, char):
        self.punc = char

    def type(self):  # Функція, що відображ. тип
        return "PuncSymbol"

    def get(self):  # Функція отримання str знаку
        return self.punc


Lab5 = Main()
