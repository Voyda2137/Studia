import random
guess = 0
liczba = random.randint(1,10)
while guess != liczba:
    print('zgaduj! ')
    guess = int(input())
print('gratulacje zgadles! liczba to', liczba)