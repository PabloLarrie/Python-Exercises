# Write a Python program to remove duplicates from Dictionary.

student_data = {1: 11, 2: 1, 3: 11, 4: 1, 5: 3, 6: 2, 7: 4, 8: 89}

result_data = {}

for k, v in student_data.items():
    if v not in result_data.values():
        result_data[k] = v


print(result_data)