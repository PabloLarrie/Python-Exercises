# Write a Python program to print the numbers of a specified list after removing even numbers from it.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista2 = []

for v in lista1:
    if v % 2 != 0:
        lista2.append(v)

print(lista2)