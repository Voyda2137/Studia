

isDivided = lambda a, num: num % a

print('Podaj liczbe:')
num = int(input())
if num > 0:
    a = 1
    arr = []
    while a != num + 1:
        if isDivided(a, num) == 0:
            arr.append(a)
        a += 1
    print('Wszystkie dzielniki liczby ', num)
    print(arr)
elif num < 0:
    a = -1
    arr = []
    while a != num - 1:
        if isDivided(a, num) == 0:
            arr.append(a)
        a -= 1
    print('Wszystkie dzielniki liczby ', num)
    print(arr)
else:
    print('0 nie ma dzielników')
