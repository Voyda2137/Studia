import time


print('Podaj liczbe: ')
liczba = int(input())
zakres = liczba
for i in range(zakres):
    print(liczba)
    time.sleep(1)
    liczba -= 1