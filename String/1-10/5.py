# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
stringa = 'abc'
stringb = 'xyz'
# Expected Result : 'xyc abz'

def gatherizer(string1, string2):
    s1 = stringa
    s2 = stringb
    new1 = s1.replace(s1[0:2], s2[0:2])
    new2 = s2.replace(s2[0:2], s1[0:2])
    final = new1 + " " + new2
    return final

print(gatherizer(stringa, stringb))

