class Bank:
    def __init__(self,name,age,money,key):
        self._name=name
        self._age=age
        self.__money=money
        self.__key=key

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def get_key(self):
        return self.__key

    def set_key(self, key):
        self.__key = key


class NewBank(Bank):
    def __init(self, name, age, money, key):
        super().init(name, age, money, key)

    @property
    def name(self):
        return self.get_name()

    @name.setter
    def name(self, name):
        self.set_name(name)

    @property
    def money(self):
        return self.get_money()

    @money.setter
    def money(self, money):
        self.set_money(money)

    @property
    def key(self):
        return self.get_key()

    @key.setter
    def key(self, key):
        self.set_key(key)


bank = NewBank("John", 30, 1000, "1234")
print(bank.money)
bank.money = 2000
print(bank.money)
print(bank.key)
bank.key = "5678"
print(bank.key)