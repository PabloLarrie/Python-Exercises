# Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5


def useless_formula(a, b):
    if a == b:
        return True
    if a + b == 5:
        return True
    if a - b == 5 or b - a == 5:
        return True


print(useless_formula(2, 3))
print(useless_formula(8, 3))
print(useless_formula(3, 8))
print(useless_formula(3, 3))
print(useless_formula(4, 3))