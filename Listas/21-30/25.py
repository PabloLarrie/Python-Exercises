# Write a Python program to select an item randomly from a list.

import random

list_first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def random_item(list):
    return random.choices(list_first)
   
print(random_item(list_first))