# Write a Python script to print a dictionary where the keys are
# numbers between 1 and 15 (both included) and the values are square of keys

d1 = {}


for v in range(1, 16):
    d1[v] = v * v
print(d1)
