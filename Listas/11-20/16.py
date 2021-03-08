#  Write a Python program to generate and print a list of first and last 5 elements
#  where the values are square of numbers between 1 and 30 (both included).


lista = []
for v in range(1, 31):
    if v < 6 or v > 26:
        lista.append(v * v)

list2 = [v * v for v in range(1, 31) if v < 6 or v > 26]

print(lista)
print(list2)