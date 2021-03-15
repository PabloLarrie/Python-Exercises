# Write a Python program to create all possible strings by using 
# 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

import itertools

vogals = ["a", "e", "i", "o", "u"]

print(list(itertools.permutations(vogals)))