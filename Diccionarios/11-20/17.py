# Write a Python program to remove duplicates from Dictionary.

student_data = {1: 11, 2: 1, 3: 11, 4: 1, 5: 3, 6: 2}
result_data = {}

for v, y in student_data.items():
    if y not in result_data.values():
        result_data[v] = y


print(result_data)