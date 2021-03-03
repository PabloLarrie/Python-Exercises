# Write a Python function that takes two lists and returns True if they have at least one common member.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
lista2 = [14, 15, 16, 17, 18, 19, 20]

final = []
for v in lista1:
    for g in lista2:
        if v == g:
            final.append(v)

print(final)
