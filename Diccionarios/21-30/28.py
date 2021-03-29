# Write a Python program to sort a list alphabetically in a dictionary.

num = {"n1": [2, 3, 1], "n2": [5, 1, 2], "n3": [3, 2, 4]}

print({k: sorted(v) for k, v in num.items()})
