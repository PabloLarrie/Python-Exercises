# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.


def getalgo(str, n):
    return (str[:2]) * n


print(getalgo("hola", 4))
print(getalgo("ha", 3))

# He entrado a mirar este porque no entendía exactamente que pedía. Mi sorpresa al ver la respuesta:


def substring_copy(str, n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]

    result = ""
    for i in range(n):
        result = result + substr
    return result


print(substring_copy("abcdef", 2))
print(substring_copy("p", 3))
