lista = []
krotka = ()
zbior = set([])
odp = ''
while odp != 'nie':
    print('Podaj liczbe:' )
    liczba = int(input())
    lista.append(liczba)
    krotka = tuple(lista)
    zbior.add(liczba)
    print('lista', lista)
    print('krotka', krotka)
    print('zbior', zbior)
    print('Jesli nie chcesz dodac kolejnej liczby napisz nie. W przeciwnym wypadku kliknij enter')
    odp = input()
