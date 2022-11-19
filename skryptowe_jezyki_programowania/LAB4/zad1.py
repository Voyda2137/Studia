import math
pi = 3.14
class circle:
    def __init__(self, numer=0, nazwa="", a=0, b=0, r=0):
        self.numer = numer
        self.nazwa = nazwa
        self.a = a
        self.b = b
        self.r = r
        self.positions = []
    def createCircle(self):
        stepSize = 0.5
        positions = self.positions
        t = 0
        while t < 2 * pi:
            number = (round(self.r * math.cos(t) + self.a, 1), round(self.r * math.sin(t) + self.b, 1)) # zaokrąglenie do 1 miejsca po przecinku
            positions.append(number)
            t += stepSize

            


circle1 = circle(1,'Kolo',3,3,3)
circle1.createCircle()
circle2 = circle(2,'Kolo',5,7,10)
circle2.createCircle()
circle3 = circle(3,'Kolo',10,10,3)
circle3.createCircle()
print(circle1.positions)
print('kolo2')
print(circle2.positions)
print('kolo3')
print(circle3.positions)
print('Podaj Wspolrzedna x:')
x = float(input())
print('Podaj wspolrzedna y')
y = float(input())
if (x, y) in circle1.positions:
    print('wspolrzedne znajduja sie w kole ', circle1.nazwa, circle1.numer)
else:
    print('wspolrzedne nie znajduja sie w kole ',circle1.nazwa, circle1.numer)
if (x, y) in circle2.positions:
    print('wspolrzedne znajduja sie w kole ', circle2.nazwa, circle2.numer)
else:
    print('wspolrzedne nie znajduja sie w kole ', circle2.nazwa, circle2.numer)
if (x, y) in circle3.positions:
    print('wspolrzedne znajduja sie w kole ', circle3.nazwa, circle3.numer)
else:
    print('wspolrzedne nie znajduja sie w kole ', circle3.nazwa, circle3.numer)