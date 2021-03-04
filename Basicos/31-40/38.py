# Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49


def calc(x, y):
    return pow((x + y), 2)


print(calc(4, 3))
