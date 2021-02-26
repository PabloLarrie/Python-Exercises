# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

import math

radio = float(input("Introduce el radio del área a calcular :"))
area = math.pi * pow(radio, 2) 
print(area)