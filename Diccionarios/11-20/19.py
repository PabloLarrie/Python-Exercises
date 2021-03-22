# Write a Python program to combine two dictionary adding values for common keys.
from collections import Counter

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
d3 = {"a": 5, "e": 200}
final = {}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


final = Counter(d1) + Counter(d2) + Counter(d3)

print(final)
