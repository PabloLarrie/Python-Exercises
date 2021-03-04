# Write a Python program to test whether a number is within 100 of 1000 or 2000.


def closeness(n):
    if n >= 900 and n <= 1100:
        return True
    if n >= 1900 and n <= 2100:
        return True
    else:
        return False


print(closeness(1900))