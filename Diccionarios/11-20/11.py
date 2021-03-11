# Write a Python program to multiply all the items in a dictionary

d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

result = 1
for v in d.values():
    result *= v
print(result)
