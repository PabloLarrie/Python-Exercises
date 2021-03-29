# Write a Python program to count the values associated with key in a dictionary.
# Expected Output:
# 6
# 2

student = [
    {"id": 1, "success": True, "name": "Lary"},
    {"id": 2, "success": False, "name": "Rabi"},
    {"id": 3, "success": True, "name": "Alex"},
]

result = 0
for v in student:
    result += len(v)
print(result)

result = 0
for v in student:
    result = 0
    result += v["id"]
print(result)

result = 0
for v in student:
    result = 0
    result += v["success"]
print(result)
