# Write a Python program to generate all permutations of a list in Python

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

permut_list = [v * g for v in lista for g in lista]

print(permut_list)
