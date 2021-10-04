# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string. 

s1 = 'w3resource'
# Expected Result : 'w3ce'
s2 = 'w3'
# Expected Result : 'w3w3'
s3 = 'w'
# Expected Result : Empty String

def mixer(string):
    if len(string) >= 2:
        return string[:2] + string[-2:]
    else:
        return "empty string"


print(mixer(s1))
print(mixer(s2))
print(mixer(s3))