# Write a Python program to add 'ing' at the end of a given string 
# (length should be at least 3). If the given string already ends with 'ing' 
# then add 'ly' instead. If the string length of the given string is less than 3, 
# leave it unchanged. 
string1 = 'abc'
# Expected Result : 'abcing'
string2 = 'string'
# Expected Result : 'stringly'
string3 = 'st'

def verbalizer(abc):
    final = ''
    if len(abc) < 3:
        return abc
    if abc[-3:] == "ing":
        final = abc + "ly"
    else:
        final = abc + "ing"
    
    return final

print(verbalizer(string1))
print(verbalizer(string2))
print(verbalizer(string3))

        