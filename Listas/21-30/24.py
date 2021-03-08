# Write a Python program to append a list to the second list

list_first = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
lista_second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 

def list_in_list(list1, list2):
    list2.append(list1)
    return list2

print(list_in_list(list_first, lista_second))