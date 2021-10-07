# Write a Python program to clone or copy a list.

sample_list = ['abc', 'xyz', 'aba', '1221', 'caac', 'moso', 'tronco', 'oso', 'huesoh', 'aa']

sample_list_copy = sample_list.copy()
sample_list_copy2 = []

for v in sample_list:
    sample_list_copy2.append(v)

print(sample_list_copy)
print(sample_list_copy2)
