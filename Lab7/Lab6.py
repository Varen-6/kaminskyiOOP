#  C13 == 6 "Визначити ієрархію амуніції лицаря. Екіпірувати лицаря. Порахувати вартість амуніції.
#  Провести сортування амуніції за вагою. Знайти елементи амуніції, що відповідає заданому діапазону цін."

#  Створити узагальнений клас та не менше 3 класів-нащадків, що описують задану варіантом область знань.
#  Створити клас, що складається з масиву об’єктів, з яким можна виконати вказані варіантом дії.
#  Необхідно обробити всі виключні ситуації, що можуть виникнути під час виконання програмного коду.\
#  Всі змінні повинні бути описані та значення їх задані у виконавчому методі.


class Ammunition:
    def __init__(self, price, weight):
        self.price = int(price)
        self.weight = int(weight)
        self.name = "Knight`s Ammunition"

    def __str__(self):
        return str("Ammunition piece: \"{}\", Weight: {}kg, Price: {} gold coins.".format(self.name, self.weight, self.price))

    def getprice(self):
        return self.price

    def getweight(self):
        return self.weight

    def getname(self):
        return self.name

    def __getitem__(self, item):
        if item == 'price':
            return self.price
        elif item == 'weight':
            return self.weight
        else:
            return None

class ArmorPiece(Ammunition):
    def __init__(self, price, weight, name):
        super().__init__(price, weight)
        self.name = name


class Weapon(Ammunition):
    def __init__(self, price, weight, name):
        super().__init__(price, weight)
        self.name = name


class Shield(Ammunition):
    def __init__(self, price, weight, name):
        super().__init__(price, weight)
        self.name = name


class Knight:
    def __init__(self, *armor):
        self.ammu = [ammu for ammu in armor]

    def ammunition_price(self):
        price = 0
        for piece in self.ammu:
            price += int(piece.price)
        print("Ammunition total price: "+str(price)+" gold coins")
        print()

    def weight_sort(self):
        self.ammu.sort(key=lambda x: x.getweight())
        print("Sorting ammunition..\n")
        self.out()

    def out(self):
        print("Knights ammunition:")
        for piece in self.ammu:
            print(piece.__str__())
        print()

    def find_by_price_range(self, minprice, maxprice):
        print("\nAmmunition in desired price range:")
        for piece in self.ammu:
            if minprice <= piece.getprice() <= maxprice:
                print(piece.__str__())
        print()


class Main:
    def __init__(self):
        Arthur = Knight(ArmorPiece(100, 5, "Сlose helmet of the Maximillian type"),
                        ArmorPiece(600, 34, "Metal Carved Breastplate"),
                        ArmorPiece(150, 8, "Metal Boots"),
                        ArmorPiece(200, 3, "Metal plated gloves"),
                        Weapon(300, 6, "Arming sword"),
                        Shield(240, 15, "Tower Shield"))
        Arthur.out()
        Arthur.ammunition_price()
        Arthur.weight_sort()
        while True:
            try:
                Arthur.find_by_price_range(int(input("Enter minimal price: ")), int(input("Enter maximal price: ")))
                return
            except TypeError:
                print("Price must be integer!\n")


if __name__ == "__main__":
    Lab6 = Main()