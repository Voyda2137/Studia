

print('Podaj ilosc rzedow choinki: ')
rows = int(input())
if rows %2 == 0:
    print('Liczba musi byc nieparzysta')
else:
    for i in range(rows):
        space_num = rows - i
        for j in range(space_num):
            print(' ', end='')
        for j in range(i * 2 + 1):
            print('*', end='')
        print('')
    for i in range(rows):
        print(' ', end='')
    print('*')
