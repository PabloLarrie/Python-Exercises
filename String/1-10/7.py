# Write a Python program to find the first appearance of the substring 
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', 
# replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
string = 'The lyrics is not that poor!\n''The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def goodizer(abc):
    new = abc
    n = new.find('not')
    v = new.find('poor')
    if n < v:
        g = new.replace(new[n:v + 4], "good")
    return g


print(goodizer(string))
