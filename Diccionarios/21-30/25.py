# Write a Python program to print a dictionary in table format.

my_dict = {"C1": [1, 2, 3], "C2": [5, 6, 7], "C3": [9, 10, 11]}

# listed = list(my_dict.items())

# print(listed[0][0], listed[1][0], listed[2][0])
# print(listed[0][1][0], listed[0][1][1], listed[0][1][2])
# print(listed[1][1][0], listed[1][1][1], listed[1][1][2])
# print(listed[2][1][0], listed[2][1][1], listed[2][1][2])

n = len(my_dict)
result = []
counter1 = True
# counter2 = True


heads = []
for k in my_dict.keys():
    if counter1 == True:
        heads.append(k)
        if len(heads) == n:
            result.append(heads)
            counter1 = False
for elem in my_dict.values():
    body = []
    # if counter2 == True:
    for j in elem:
        body.append(j)
    result.append(body)


for v in result:
    print(v)
