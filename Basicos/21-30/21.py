# Write a Python program to find whether a given number
# (accept from the user) is even or odd, print out an appropriate message to the user.


def parity(n):
    if n % 2 == 0:
        return "This number is even"
    else:
        return "This number is odd"


print(parity(10))