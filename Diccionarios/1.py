# Write a Python script to sort (ascending and descending) a dictionary by value

my_dicc = {"Hola": "Adiós", "MiCasa": "TuCapa", "Quien": "puma", 20: "voy"}
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

lista_de_tuplas_ass = sorted(d.items(), key=lambda x: x[1])
lista_de_tuplas_des = sorted(d.items(), key=lambda x: x[1], reverse=True)
new_dicc = dict(lista_de_tuplas_ass)
new_dicc2 = dict(lista_de_tuplas_des)

print(new_dicc)
print(new_dicc2)