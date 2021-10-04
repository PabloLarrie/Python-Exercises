# Write a Python program to change a given string to a new string 
# where the first and last chars have been exchanged

hoss = 'hola me quiero salir de aquí'

def exchanger (abc):
    g = abc[0]
    i = abc[-1]
    h = abc.replace(abc[0], i)
    return abc.replace(h[-1], g)

print(exchanger(hoss))