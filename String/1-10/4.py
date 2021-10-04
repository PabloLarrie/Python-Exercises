# Write a Python program to get a string from a given string where all occurrences 
# of its first char have been changed to '$', except the first char itself. 
strings = 'restart'
# Expected Result : 'resta$t'

def replacizer(string):
    new = string.replace(string[0], '$')
    new2 = new.replace(new[0], string[0], 1)
    return new2

print(replacizer(strings))
