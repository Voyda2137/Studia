import numpy as np
import random
import statistics

lista = []

for i in range(20):
    lista.append(random.randint(0, 5))
srednia = sum(lista)/len(lista)
print('lista', lista)

print('co 2', lista[::2])

print('mediana', statistics.median(lista))
print('srednia', srednia)

lista_unikalna = np.array(lista)
lista_unikalna = np.unique(lista_unikalna)
lista_unikalna = lista_unikalna.tolist()
print('unikalne liczby ', lista_unikalna)

for x in range(len(lista)):
    if 0 in lista:
        lista.remove(0)
print(lista)


