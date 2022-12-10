class drink():
    def __init__(self, name=str(), price=int(), alc=int(), capacity=int()):
        self.name = name
        self.price = price
        self.alc = alc
        self.capacity = capacity

    def __add__(self, other):
        newDrink = drink("", 0, 0, 0)
        newDrink.name = self.name + " z " + other.name
        newDrink.price = self.price + other.price
        newDrink.alc = round(((self.capacity * self.alc) + (other.capacity *
                                                            other.alc))/(self.capacity + other.capacity))
        newDrink.capacity = self.capacity + other.capacity
        print('Nazwa nowego drinka: ', newDrink.name, ' Cena: ', newDrink.price,
              ' Zawartość alkoholu: ', newDrink.alc, '% ', 'Jego pojemność: ', newDrink.capacity)
        return newDrink

    def manyDrinks(self, amm):
        multipleDrinks = drink("", 0, 0, 0)
        multipleDrinks.name = self.name
        multipleDrinks.price = self.price * amm
        multipleDrinks.capacity = self.capacity * amm
        multipleDrinks.alc = self.alc
        print('Cena', amm, ' drinków typu', multipleDrinks.name,
              multipleDrinks.price, 'zł ich łączna pojemność:', multipleDrinks.capacity, 'ml')

    def __str__(self):
        print('Nazwa drinka: ', self.name, ' Cena: ', self.price,
              ' Zawartość alkoholu: ', self.alc, '% ', 'Jego pojemność: ', self.capacity)

    def __lt__(self, other):
        if self.price == 0:
            return False
        elif other.price == 0:
            return True
        else:
            return (self.alc / self.price) < (other.alc / other.price)


vodka = drink('wódka', 8, 40, 50)
rum = drink('rum', 9, 60, 50)
cola = drink('cola', 2, 0, 100)
ice = drink('lód', 0, 0, 30)
wine = drink('wino', 5, 15, 100)
whiskey = drink('whiskey', 12, 40, 50)

drink1 = vodka + rum
drink2 = vodka + whiskey
drink3 = whiskey + ice
drink4 = cola + ice
manyVodkas = drink(vodka.manyDrinks(8))
drink(cola.__str__())
arr = [drink1, drink2, drink3, drink4]
arr.sort()
for i in arr:
    drink(i.__str__())
