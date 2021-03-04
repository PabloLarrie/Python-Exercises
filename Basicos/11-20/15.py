# Write a Python program to get the volume of a sphere with radius 6.
import math

radius = int(input("Declara el radio :"))
volume = 4 / 3 * math.pi * pow(radius, 3)

print(volume)