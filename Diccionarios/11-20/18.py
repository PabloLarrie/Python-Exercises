# Write a Python program to check a dictionary is empty or not.

d = {1: 11, 2: 1, 3: 11, 4: 1, 5: 3, 6: 2}
d2 = {}


def whether_is_empty_or_not(listt):
    return True if listt.items() else False


print(whether_is_empty_or_not(d))
print(whether_is_empty_or_not(d2))