# Write a Python function that takes two lists and returns True if they have at least one common member.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
lista2 = [14, 14, 15, 16, 17, 18, 19, 20]
set3 = {2, 90, 48, 12, 6, 14}

set1 = set(lista1)
set2 = set(lista2)

final = set()
for v in lista1:
    for g in lista2:
        if v == g:
            final.add(v)

final = {v for v in lista1 for g in lista2 if v == g}

print(final)

# Para calcular los comunes
print(bool(set1.intersection(set2)))

# Para calcular las diferencias entre ambos
print(set1.difference(set2))
print(set2.difference(set1))

# Para hacer merge entre ambos
print(set1 | set2)

# Si se quiere hacer con muchos sets
# Intersection
print(set1 & set3 & set2)

# Differencia
print(set1 ^ set2)

# Merge
print(set1 | set2)