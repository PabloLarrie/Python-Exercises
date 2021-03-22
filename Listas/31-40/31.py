# Write a Python program to count the number of elements in a list within a specified range

list_first = [1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 13, 7, 8, 9, 10, 11, 11, 12, 13]


print({v: list_first.count(v) for v in range(int(input("inicio: ")))})