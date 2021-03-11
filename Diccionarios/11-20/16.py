# Write a Python program to get a dictionary from an object's fields.


# Ni idea de como se hacía esto !!


class object1(object):
    def __init__(self):
        self.x = "red"
        self.y = "yellow"
        self.z = "green"

    def nothing(self):
        pass


test = object1()

print(test.__dict__)