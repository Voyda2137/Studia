add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b


def calculator(num, a, b):
    if num == 1:
        print('Wynik dodawania: ', add(a, b))
    elif num == 2:
        print('Wynik odejmowania: ', subtract(a, b))
    elif num == 3:
        print('Wynik mnozenia: ', multiply(a, b))
    elif num == 4:
        if b != 0:
            print('Wynik dzielenia: ', divide(a, b))
        else:
            print('Nie mozna dzielic przez 0')

print('Wybierz co chcesz zrobic')
print('1. Dodawanie 2. Odejmowanie 3. Mnozenie 4. Dzielenie')
num = int(input())
if num in [1, 2, 3, 4]:
    print('Podaj a:')
    a = int(input())
    print('Podaj b:')
    b = int(input())
    calculator(num, a, b)
else:
    print('Wybrano nieprawidlowa opcje')