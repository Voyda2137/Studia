import time


def timer_func(func):
    def wrap_func(*args):  # przekazanie argumentów funkcji jako tablicy
        t1 = time.time() * 1000
        result = func(*args)
        t2 = time.time() * 1000  # czas w ms
        print(f'Funkcja wykonala sie w {(t2 - t1)}ms')
        return result

    return wrap_func


@timer_func
def factorial(n, fact):
    for i in range(1, n + 1):
        fact = fact * i
    return fact


@timer_func
def recur_factorial(n):
    if n != 1:
        return n * recur_factorial(n - 1)
    else:
        return n


# lambda z rekursją
fctLambda = lambda num: 1 if num <= 1 else num * fctLambda(num - 1)

fact = 1
print('Podaj liczbe:')
n = int(input())
if n > 0:
    print('Silnia z tradycyjnej funkcji: ', factorial(n, fact))

    print('Silnia z rekursji:', recur_factorial(n))

    print('Silnia z lambdy: ', fctLambda(n))
elif n == 0:
    print('Silnia jest rowna 1')
else:
    print('Liczba nie moze byc mniejsza od 0')
