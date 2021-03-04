# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.


def stringing(strs):
    if strs[:2] == "Is" or strs[:2] == "is":
        return strs
    else:
        return "Is " + strs


print(stringing("Hello my life"))