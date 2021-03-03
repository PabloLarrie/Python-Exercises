# Write a Python program to get the largest number from a list.

listt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 3333]

print(max(listt))

largest = listt[0]
for v in listt:
    if v >= largest:
        largest = v

print(largest)

g = sorted(listt)
        
print(g[-1])
