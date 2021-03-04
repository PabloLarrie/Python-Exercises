# Write a Python program to display your details like name, age, address in three different lines


def details(name, age, adress):
    g = [name, age, adress]
    for v in g:
        print(v)


details("Pablo", 29, "Calle de la piruleta")