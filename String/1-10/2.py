# Write a Python program to count the number of characters (character frequency) in a string.
string = "google.com'"
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

print({v: string.count(v) for v in string})
