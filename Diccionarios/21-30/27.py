# Write a Python program to convert a list into a nested dictionary of keys.
# {1: {2: {3: {4: {}}}}}

num_list = [1, 2, 3, 4]

n = 0
count = num_list[n]


def nesterizer(lista):
    result = {}
    for v in lista:
        if v == :
            result[v] = nesterizer()
            
            

print(nesterizer(num_list))
