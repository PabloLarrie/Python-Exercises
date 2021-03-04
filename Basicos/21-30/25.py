# Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


def contained(list, n):
    if n in list:
        return "Mu bien maxote"
    else:
        "Pa la prósima"


print(contained([1, 5, 8, 3], 3))
