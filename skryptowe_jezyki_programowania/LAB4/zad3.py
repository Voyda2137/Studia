class drink():
    def __init__(self, name=str(), price=int(), alc=int(), capacity=int()):
        self.name = name
        self.price = price
        self.alc = alc
        self.capacity = capacity
    def __add__(self, other):
        name = self.name + " z " + other.name
        price = self.price + other.price
        alc = round(((self.capacity * self.alc) + (other.capacity * other.alc))/(self.capacity + other.capacity))
        capacity = self.capacity + other.capacity
        print('Nazwa nowego drinka: ', name, ' Cena: ', price, ' Zawartość alkoholu: ', alc,'% ', 'Jego pojemność: ', capacity)
    def manyDrinks(self, amm):
        price = self.price * amm
        capacity = self.capacity * amm
    def __str__(self):
        print('Nazwa drinka: ', self.name, ' Cena: ', self.price, ' Zawartość alkoholu: ', self.alc,'% ', 'Jego pojemność: ', self.capacity)
    def __lt__(self, other):
        return self.alc  < other.alc 
vodka = drink('wódka', 8, 40, 50)
rum = drink('rum', 9, 60, 50)
cola = drink('cola', 2, 0, 100)
ice = drink('lód', 0, 0, 30)
wine = drink('wino', 5, 15, 100)
whiskey = drink('whiskey', 12, 40, 50)        

drink(vodka.__add__(cola))
drink(vodka.manyDrinks(8))
drink(cola.__str__())
arr = [vodka, rum, cola, ice, wine, whiskey]
arr.sort()

