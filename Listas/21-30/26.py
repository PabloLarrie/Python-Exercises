# Write a python program to check whether two lists are circularly identical.

list_first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
list_second = [7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6] 

# def circular_identity(list1, list2):
#     if sorted(list_first) == sorted(list_second):
#         return True

# print(circular_identity(list_first, list_second)) 


def check_circ_identity(list, list2):
    if (' '.join(str(list_first))) in (' '.join(str(list_first))) * 2:
        return True

print(check_circ_identity(list_first, list_second))


# g = (' '.join(str(list_first)))

# print(type(g))

# g = (' '.join(map(str ,list_first)))

# print(type(g))

# print(g)