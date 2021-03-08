#  Write a Python script to check whether a given key already exists in a dictionary.

my_dicc = {"Hola": "Adiós", "MiCasa": "TuCapa", "Quien": "puma", 20:"voy"}
key = "MiCasa"

def sipi(lista, clave):
    if clave in my_dicc:
        return True

print(sipi(my_dicc, key))

