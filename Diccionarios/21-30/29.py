# Write a Python program to remove spaces from dictionary keys

data = {"S  001": ["Math", "Science"], "S    002": ["Math", "English"]}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}

print({k.replace(" ", ""): v for k, v in data.items()})