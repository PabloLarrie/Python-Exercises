# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
data = {"1": ["a", "b"], "2": ["c", "d"]}
# Expected Output:
# ac
# ad
# bc
# bd

result = [v for v in data.values()]


print(result[0][0] + result[1][0])
print(result[0][0] + result[1][1])
print(result[0][1] + result[1][0])
print(result[0][1] + result[1][1])