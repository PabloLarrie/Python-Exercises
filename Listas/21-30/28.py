# Write a Python program to find the second largest number in a list

list_first = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def runner_up(lista):
    maxi = sorted(set(lista))  # si el mínimo vale repetido pues se quita el "set"
    return maxi[-2]


print(runner_up(list_first))
