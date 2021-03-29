# Write a Python program to get the top three items in a shop
data = {"item1": 45.50, "item2": 35, "item3": 41.30, "item4": 55, "item5": 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

print(sorted(data.items(), key=lambda x: x[1], reverse=True)[0:3])
