# Write a Python program access the index of a list

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list_dex = [(i, v) for i, v in enumerate(lista)]

for v in list_dex:
    print(v)