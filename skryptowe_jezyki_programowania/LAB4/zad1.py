import math


class circle:
    def __init__(self, numer=0, nazwa="", a=0, b=0, r=0):
        self.numer = numer
        self.nazwa = nazwa
        self.a = a
        self.b = b
        self.r = r


circle1 = circle(1, 'Kolo', 3, 3, 3)
circle2 = circle(2, 'Kolo', 5, 7, 10)
circle3 = circle(3, 'Kolo', 10, 10, 3)

x = int(input('Podaj x: '))
y = int(input('Podaj y: '))
warunek1 = pow(x - circle1.a, 2) + pow(y - circle1.b, 2) < pow(circle1.r, 2)
warunek2 = pow(x - circle2.a, 2) + pow(y - circle2.b, 2) < pow(circle2.r, 2)
warunek3 = pow(x - circle3.a, 2) + pow(y - circle3.b, 2) < pow(circle3.r, 2)
if warunek1 or warunek2 or warunek3:
    print('Punkt znajduje się w kole')
else:
    print('Punkt nie znajduje się w kole')
