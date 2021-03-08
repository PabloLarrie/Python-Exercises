# Write a Python program to get the smallest number from a list.

listt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 3333]

print(min(listt))

shortest = listt[0]
for v in listt:
    if v <= shortest:
        shortest = v
print(shortest)
