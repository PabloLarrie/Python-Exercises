# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

sample_list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
sample_list2 = ["Red", "Red", "Red", "Red", "Red", "Green", "White", "Black", "Pink", "Yellow"]

indexes_to_delete = [5, 4, 0]

for i in indexes_to_delete:
    sample_list.pop(i)

print(sample_list)

final_list = []
for i, v in enumerate(sample_list2):
    if i not in indexes_to_delete:
        final_list.append(v)

final_list = [v for i, v in enumerate(sample_list2) if i not in indexes_to_delete]

print(final_list)
