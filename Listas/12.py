# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

sample_list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
sample_list2 = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

sample_list.pop(5)
sample_list.pop(4)
sample_list.pop(0)

print(sample_list)

final_list = []
for v in sample_list2:
    if v == sample_list2[0]:
        pass
    elif v == sample_list2[4]:
        pass
    elif v == sample_list2[5]:
        pass
    else:
        final_list.append(v)

print(final_list)