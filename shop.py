from random import *
class Busket:
    def __init__(self):
        self.products = []
        self.total_price = 0

    def add_product(self, product):
        self.products.append(product)
        #self.total_price += product.get_price

    def receipt(self):
        for prod in self.products:
            self.total_price += prod.get_price()

    def del_prod(self, name):
        for indx, prod in enumerate(self.products):
            if name.srtip() in prod.get_name:
                del self.products[indx]

    def del_all(self):
        self.products = []

    def show(self):
        print("________")
        for ind, i in enumerate(self.products):
            print(ind, ':', i)



class Products:
    def __init__(self, name, price, rating):
        self.__name = name
        self.__price = price
        self.__rating = rating

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_info(self):
        return [self.__name, self.__price, self.__rating]


class Category:
    def __init__(self):
        self.name = None
        self.products = []

    def add_products(self, prods):
        for pr in prods:
            ran = randint(70, 670)
            ran_ = randint(0, 10)
            pr_inf = Products(pr, ran, ran_)
            self.products.append(pr_inf.get_info())

    def get_products(self):
        return self.products

    def show_(self):
        print(self.name,":" )
        print("___________________")
        for ind, dfs in enumerate(self.products):
            print(ind, ":", dfs)
class User:
    def __init__(self, login, password):
        self.busket = Busket()
        self.money = 20000

        if login == "user" and password == '123':
            self.login = login
            self.password = password
            print("Вы вошли!")

    def add_prod(self, prod):
        self.busket.add_product(prod)

    # self.busket.receipt()

    def buy_all(self):
        self.money -= self.busket.total_price
        self.busket.show()
        print(f"Ваш баланс :{self.money}")

    def buy_sm(self, prod_name):
        for hz in self.busket.products:
            if hz == prod_name:
                self.money -= prod_name.get_price()
                print(self.money)
            else:
                print("Error")


fruits = ['Бананы', 'Киви', 'Яблоки', 'Апельсины', ]
vegetables = ['Морковь', 'Свекла', 'Сельдерей', 'Салат зеленый', ]
juice = ['Сок DaDa Яблоко и мята', 'Сок Gracio Ананас',
         'Сок Gracio Гранат', 'Сок Olevi тыквенно-яблочный',
         'Нектар Gelios Вишня', 'Нектар Gelios Гранат',
         'Нектар Gelios Абрикос с мякотью', 'Сок Telli апельсиновый', ]
meet = ['Стейк свиной Globus', 'Ветчина «Империя вкуса», с индейкой',
        'Ветчина «Микоян», «Московская»', 'Колбаса вареная', ]

# ДОБАВЛЯЕМ КАТЕГОРИИ И ПРОДУКТЫ
_fruits = Category()
_fruits.name = 'фрукты'
_vegetables = Category()
_vegetables.name = 'овощи'
_juice = Category()
_juice.name = 'соки'
_meat = Category()
_meat.name = 'мясо'

# КАТЕГОРИИ
_fruits.add_products(fruits)
_vegetables.add_products(vegetables)
_juice.add_products(juice)
_meat.add_products(meet)

# СОЗДАЕМ ЮЗЕРА И ЗАПРАШИВАЕМ ДАННЫЕ
# ГЛАВНЫЙ ЦИКЛ
# ПОКАЗЫВАЕМ КАТЕГОРИИ
# ПРЕДЛАГАЕМ ВЫБРАТЬ

def vibor(L):
    L.show_()
    item = input("хотите что то из этого приобрести ?")
    print(L.get_products())
    for o in L.get_products():
        if item == o[0]:
            chelovek.add_prod(o[0])
            chelovek.busket.show()
            chelovek.busket.total_price += int(o[1])
            print(chelovek.busket.total_price)
            fd = input("Хотите купить содержимое ? [yes/no]")
            if fd == "yes":
                chelovek.money -= chelovek.busket.total_price
                print(f"ваш баланс :{chelovek.money}")
                chelovek.busket.del_all()
                break
            elif fd == "no":
                d = input("Категория желаемого товара?")
                if d == _juice.name:
                    vibor(_juice)
                elif d == _meat.name:
                    vibor(_meat)
                elif d == _fruits.name:
                    vibor(_fruits)
                elif d == _vegetables.name:
                    vibor(_vegetables)
                else:
                    print('нормально введи!')
            else:
                pass
            break
        else:
            pass



chelovek = User('user', '123')

while True:
    hg = input("хотите что то приобрести ? [yes/no]")
    if hg == 'yes':
        vnv = input("Категория желаемого товара?")
        if vnv == _juice.name:
            vibor(_juice)
        elif vnv == _meat.name:
            vibor(_meat)
        elif vnv == _fruits.name:
            vibor(_fruits)
        elif vnv == _vegetables.name:
            vibor(_vegetables)
        else:
            print('нормально введи!')
    elif hg == "no":
        print("До встречи!")
        break
    else:
        print('Error')
        break