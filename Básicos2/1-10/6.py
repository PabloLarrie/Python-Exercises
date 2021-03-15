# Write a Python program to print a long text, convert the string 
# to a list and print all the words and their frequencies.

long_text = """This is a quite long, long long text.
It is long because it is not short.
And it is not short because no it is not long.
"""

list_dex = [(i, v) for i, v in enumerate(list(long_text.split(" ")))]

print(long_text, list_dex)