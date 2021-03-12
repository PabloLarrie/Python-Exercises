# Write a Python program to concatenate all elements in a list into a string and return it.


def concatenizer(list):
    to_str = [str(v) for v in list]
    return "".join(to_str)


print(concatenizer(["alabama", "c", "casa"]))
print(concatenizer([1, 3, 54, 2, 5]))