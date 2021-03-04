# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum


def critical(a, b, c):
    h = a + b + c
    if a == b == c:
        return h * 3
    else:
        return h


print(critical(3, 3, 3))
