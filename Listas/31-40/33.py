# Write a Python program to generate all sublists of a list. 

lista = [2, 3, [2, 4, [2,6, [3, 0]]], 5]

for v in lista:
    if type(v) == list:
        print(v)