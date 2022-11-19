from enum import Enum

class Car:
    def __init__(self, model=str(), color=str(), hp=int(), condition='new' ):
        self.model = model
        self.color = color
        self.hp = hp
        self.condition = condition
    def displayCar(self):
        print(self.model, self.color, self.hp, self.condition)
    def driveCar(self):
        self.condition = 'used'
class ElectricCar(Car):
    def __init__(self, model, color, hp, condition, batteryType):
        Car.__init__(self, model, color, hp, condition)
        self.batteryType = batteryType
    def displayCar(self):
        print(self.model, self.color, self.hp, self.condition, self.batteryType)
class BatteryType(Enum):
    lithium_ion = 1
    nickel_metal_hydride = 2
    lead_acid = 3
    ultracapacitor = 4

car = Car('bugatti', 'red', 300)
car.displayCar()
car.driveCar()
car.displayCar()
car = ElectricCar(car.model, car.color, car.hp, car.condition, BatteryType(1).name)
car.displayCar()