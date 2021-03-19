#  Write a Python program to get unique values from a list.

list_first = [1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 13, 7, 8, 9, 10, 11, 11, 12, 13] 

to_delete = [v for v in list_first if list_first.count(v) > 1]

set1 = set(list_first)
set2 = set(to_delete)

print(set1 ^ set2)
