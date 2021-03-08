# Write a Python program to find the second smallest number in a list.
list_first = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 

def runner_down(list):
    minim = sorted(set(list_first)) #si el mínimo vale repetido pues se quita el "set"
    return minim[1]

print(runner_down(list_first))
