# Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


def contained(lista, n):
    return n in lista


print(contained([1, 5, 8, 3], 3))
