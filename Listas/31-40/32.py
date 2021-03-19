# Write a Python program to check whether a list contains a sublist.

lista = [2, 3, [2, 4, [2,6, [3, 0]]]]

for v in lista:
    if type(v) == list:
        print(True)

     
