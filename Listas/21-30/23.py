# Write a Python program to flatten a shallow list.

shallow_list = [[1, 0], [3, 1], [[2, 4], 5]]

def shallowed(list):
    shallowed_list = [g for v in shallow_list for g in v]
    return shallow_list
    
print(shallowed(shallow_list))

