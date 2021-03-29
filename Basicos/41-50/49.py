# Write a Python program to list all files in a directory in Python.

from os import listdir
from os.path import isfile, join, split
import os


directorio_actual = os.path.abspath(__file__)
# '/home/pablo/proyectos/Ejercicios Python/Basicos/41-50/49.py'
g = split(directorio_actual)

files_list = [f for f in listdir(g[0]) if isfile(join("/home/Projects", f))]

print(files_list)