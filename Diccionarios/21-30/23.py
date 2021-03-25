# Write a Python program to combine values in python list of dictionaries.
from collections import Counter

data = [
    {"item": "item1", "amount": 400},
    {"item": "item2", "amount": 300},
    {"item": "item1", "amount": 750},
]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

result = list({v for v in data[0].values()})
result2 = list({v for v in data[1].values()})
result3 = list({v for v in data[2].values()})

result_final = {}
result_final[result[0]] = result[1]
result_final[result2[0]] = result2[1]
result_final[result3[0]] = result3[1]

print(result, result2, result3)
print(result_final)

# print(suma_dicts(result)