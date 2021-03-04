# Write a Python program to create a histogram from a given list of integers.


def histogram(list):
    for v in list:
        print("*" * v)


histogram([1, 2, 4, 6, 7])