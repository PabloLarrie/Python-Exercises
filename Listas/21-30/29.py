#  Write a Python program to get unique values from a list.

list_first = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 

def uniqueness(list):
    list_second = []
    for v in list_first:
        for g in list_first:
            if g not in list_first:
                list_second.append(g)
    return list_second

print(list_first)
print(uniqueness(list_first))

# def uniqueness(list):
#     unique_list = [g for v in list_first for g in list_first if g not in list_first]
#     return unique_list

# print(uniqueness(list_first)) 