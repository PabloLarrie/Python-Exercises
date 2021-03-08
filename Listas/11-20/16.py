#  Write a Python program to generate and print a list of first and last 5 elements
#  where the values are square of numbers between 1 and 30 (both included).


lista = []
for i, v in enumerate(range(30)):
    if v != 0 and i < 6 or i > 25:
        lista.append(v * v)    

list2 = [ (v * v) for i, v in enumerate(range(30)) if v != 0 and i < 6 or i > 25 ]

print(lista)
print(list2)