# Write a Python program to remove the nth index character from a nonempty string.

string = "Write a Python program to remove the nth index character"

def removizer(abc, n):
    return abc.replace(abc[n], "", 1)

print(removizer(string, 4))