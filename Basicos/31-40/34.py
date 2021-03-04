# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.


def summ(a, b):
    g = a + b
    if g >= 15 and g <= 20:
        return 20
    else:
        return a + b


print(summ(4, 2))
print(summ(10, 7))