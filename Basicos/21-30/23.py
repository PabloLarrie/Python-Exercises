# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.


def getalgo(string, n):
    return (string[:2]) * n


print(getalgo("hola", 4))
print(getalgo("ha", 3))
print(getalgo("abcdef", 2))
print(getalgo("p", 3))
