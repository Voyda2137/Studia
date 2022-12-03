class drink:
    def __init__(self, name=str(), price=int(), alc=int(), capacity=int()):
        self.name = name
        self.price = price
        self.alc = alc
        self.capacity = capacity

vodka = drink('wódka', 8, 40, 50)
rum = drink('rum', 9, 60, 50)
cola = drink('cola', 2, 0 ,100)
ice = drink('lód', 0, 0, 30)

class newDrink:
    def __init__(self, name, price, alc, capacity):
        drink.__init__(self, name, price, alc, capacity)
        self.name = 