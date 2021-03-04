# Write a Python program to shuffle and print a specified list.

import random

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista2 = []
lista3 = lista1.copy()  # CUIDADO; solo se copia el valor en campos inmutables si lo hacemos a mano como en el for que has hecho o con un .copy()

random.shuffle(lista1)
print(lista1)

print(lista3)

for v in lista1:
    lista2.append(v)
print(lista2)

random.shuffle(lista3)
print(lista3)