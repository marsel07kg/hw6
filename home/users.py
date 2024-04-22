from bank import NewBank
class bakai_bank(NewBank):
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

bank = NewBank("marsel", 300, 'денег нету :(', "3223")
print(bank.money)
bank.money = 2000
print(bank.money)
print(bank.key)
bank.key = "5678"
print(bank.key)