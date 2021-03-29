# Write a Python program to combine values in python list of dictionaries.
from collections import Counter

data = [
    {"item": "item1", "amount": 400},
    {"item": "item2", "amount": 300},
    {"item": "item1", "amount": 750},
]

result = {}

for l in range(len(data)):
    for k, v in data[l].items():
        if v in result:
            result[v] += data[l]["amount"]
            break
        else:
            result[v] = data[l]["amount"]
            break


print(result)
