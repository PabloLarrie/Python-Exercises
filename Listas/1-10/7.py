# Write a Python program to remove duplicates from a list.

sample_list = ['abc', 'xyz', 'aba', '1221', 'caac', 'moso', 'tronco', 'oso', 'huesoh', 'aa', 'xyz', 'caac']

# final_list = []
# for listt in sample_list:
#     if listt not in final_list:
#         final_list.append(listt)

final_list = list(set(sample_list))

print(final_list)