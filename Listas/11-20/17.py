# Write a Python program to generate and print a list except for the first 5 elements, 
# where the values are square of numbers between 1 and 30 (both included).

list2 = [ (v * v) for i, v in enumerate(range(30)) if i > 5 ]

print(list2)