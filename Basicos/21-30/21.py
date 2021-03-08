# Write a Python program to find whether a given number
# (accept from the user) is even or odd, print out an appropriate message to the user.


def parity(n):
    return "This number is even" if n % 2 == 0 else "This number is odd"


print(parity(10))