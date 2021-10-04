lista = """Write a Python function that takes a list of words 
and returns the longest word and the length of the longest one."""
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

def longanizer(abc):
    g = max(list(abc.split(" ")), key=len)
    return g + " " + str(len(g))

print(longanizer(lista))
