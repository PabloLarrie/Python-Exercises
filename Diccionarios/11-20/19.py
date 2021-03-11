# Write a Python program to combine two dictionary adding values for common keys.
from collections import Counter

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
d3 = {}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


d3 = Counter(d1) + Counter(d2)

print(d3)

# def combinizer(list1, list2):
#         for k, v in list1.items():
#             d3[k] = v
#         return d3


# print(combinizer(d1, d2))