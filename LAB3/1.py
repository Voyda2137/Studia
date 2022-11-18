

def collatz(number):
    if number % 2 == 0:
        result = number /2
        print('Liczba jest parzysta, a podzielona przez 2 jest rowna: ', result)
        return result
    elif number % 2 != 0:
        result = number * 3 + 1
        print('Liczba jest nieparzysta, a po dzialaniu jest rowna: ', result)
        return result
res = 0

print('Podaj liczbe:')
number = int(input())

while number != 1:
    number = collatz(number)
    if number == 1:
        print('Liczba jest rowna 1, a program sie konczy')