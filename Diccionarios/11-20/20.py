# Write a Python program to print all unique values in a dictionary.
from collections import Counter

diccionario = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"},
]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

#No me ha gustado nada hacerlo así D:

results = []

for v in diccionario:
    res = list(v.values())
    for f in res:
        results.append(f)

print(set(results))
