# Write a Python program to test whether a number is within 100 of 1000 or 2000.


def closeness(n):
    return 900 <= n <= 1100 or 1900 <= n <= 2100


print(closeness(1900))