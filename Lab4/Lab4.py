# C11 == 8 "Визначити клас меблі, який складається як мінімум з 5-и полів."
# Створити клас із виконавчим методом, в якому створити масив з об’єктів класу визначеному варіантом.
# Відсортувати масив, за одним з полів, за зростанням, а за іншим, за спаданням використавши при цьому стандартні засоби сортування.
# Всі змінні повинні бути описані та значення їх задані у виконавчому методі.
# Код повинен бути детально задокументований.


class Furniture():
    """Клас меблів"""
    def __init__(self, name, price, color, material, country_manufacturer):
        self.name = name
        self.price = price
        self.color = color
        self.material = material
        self.country_manufacturer = country_manufacturer


class Main():
    """Основний клас"""
    def __init__(self):
        """Виконавчий метод"""

        # Задання об’єктів "меблі":
        try:
            coffee_table = Furniture(name="Журнальний столик", price="200$", color="Прозорий", material="Скло", country_manufacturer="Білорусь")
            stool = Furniture(name="Табуретка", price="50$", color="Білий", material="Дерево", country_manufacturer="Україна")
            chair = Furniture(name="Стілець", price="75$", color="Червоний", material="Пластик", country_manufacturer="Китай")
            armchair = Furniture(name="Крісло офісне", price="400$", color="Чорний", material="Шкіра", country_manufacturer="США")
            dining_table = Furniture(name="Кухонний стіл", price="300$", color="Коричневий", material="Дерево", country_manufacturer="Польща")

        except TypeError:
            print("Ви забули вказати одне або декілька полів!")
            return

        # Створення масиву об’єктів "Меблі"
        furniture_list = [coffee_table, stool, chair, armchair, dining_table]

        try:
            # Сортування масиву об’єктів "Меблі" за полем "Вартість" за зростанням:
            furniture_list.sort(key=lambda x: int(x.price.replace("$", "")), reverse=False)

            # Вивід відсортованого масиву:
            print("\nМасив об’єктів \"Меблі\", відсортований за полем \"Вартість\" за зростанням:")
            for elem in furniture_list:
                print(elem.name + " - " + elem.price)

        except ValueError:
            print("Вартість треба задавати у форматі <Число>$")
            return

        # Сортування масиву об’єктів "Меблі" за полем "Країна виробник" за спаданням:
        furniture_list.sort(key=lambda x: x.country_manufacturer, reverse=True)

        # Вивід відсортованого масиву:
        print("\nМасив об’єктів \"Меблі\", відсортований за полем \"Країна виробник\" за спаданням:")
        for elem in furniture_list:
            print(elem.name + " - " + elem.country_manufacturer)


main = Main()
