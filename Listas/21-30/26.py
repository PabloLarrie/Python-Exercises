# Write a python program to check whether two lists are circularly identical.

import timeit


list_first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
list_second = [7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def check_circ_identity(lista, list2):
    if ' '.join(map(str, lista)) in ' '.join(map(str, list2 * 2)):
        return True
    else:
        return False


def check_circ_identity_2(lista, list2):
    size = len(lista)
    if size != len(list2):
        return False
    value = lista[0]
    try:
        index = list2.index(value)
    except ValueError:
        return False

    ordered = [list2[i] if i < size else list2[i - size] for i in range(index, index + size)]
    return ordered == lista

print(timeit.timeit(lambda: check_circ_identity(list_first, list_second)))
print(timeit.timeit(lambda: check_circ_identity_2(list_first, list_second)))
