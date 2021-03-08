#  Write a Python program to get the difference between the two lists

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

set1 = set(lista1)
set2 = set(lista2)

print(set1 ^ set2)
print(set2 ^ set1)