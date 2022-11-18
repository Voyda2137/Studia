

print('Podaj długość promienia: ')
radius = int(input())
area = 0
print('dlugosc to ', radius)
if radius <= 0:
    print('Podana wartosc nie moze byc mniejsza lub rowna 0')
else:
    area = 3.14 * pow(radius,2)
    print('pole okregu to: ', area)
