#  Write a Python script to check whether a given key already exists in a dictionary.

my_dicc = {"Hola": "Adiós", "MiCasa": "TuCapa", "Quien": "puma", 20: "voy"}
key = "MiCasa"


def sipi(lista, clave):
    return clave in lista


print(sipi(my_dicc, key))
