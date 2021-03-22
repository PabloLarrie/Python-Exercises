# Write a Python program to add two objects if both objects are an integer type.


def addicted(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    print(a + b)


addicted(1, 4)
addicted(4, "hola")