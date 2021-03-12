# Write a Python program to print all even numbers from a given numbers list in
# the same order and stop the printing if any numbers that come after 237 in the sequence.
import random

n = 100

numbers = [random.randint(0, 1000) for _ in range(n)]

g = random.randint(0, n - 1)

numbers.insert(g, 237)


number_list = []
impares = 0
for v in numbers:
    if v == 237:
        break
    elif v % 2 == 0:
        number_list.append(v)
    else:
        impares += 1


pares = len(number_list)
indice = pares + impares

print(number_list)
print(impares)
print(indice)
print(g)
print(indice == g)
