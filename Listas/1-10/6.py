# Write a Python program to get a list, sorted in increasing order by 
# the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sample_listed_list = []
for tupla in sample_list:
    sample_listed_list.append(list(tupla))

reverse_list = []
for lists in sample_listed_list:
    reverse_list.append(lists.reverse())

sorted_list = sorted(sample_listed_list)

reverse_list2 = []
for lists2 in sorted_list:
    reverse_list2.append(lists2.reverse())

definitive_killing_awesome_destroyer_mospowerfull_list = []
for tuplas in sorted_list:
    definitive_killing_awesome_destroyer_mospowerfull_list.append(tuple(tuplas))

# print(sample_listed_list)
# print(reverse_list)
# print(sorted_list)
# print(reverse_list2)
print(definitive_killing_awesome_destroyer_mospowerfull_list)

