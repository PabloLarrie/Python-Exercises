# Write a Python script to concatenate following dictionaries to create a new one.

# Sample Dictionary :
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)

final = {**dic1, **dic2, **dic3}

print(dic4)
print(final)