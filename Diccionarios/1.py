# Write a Python script to sort (ascending and descending) a dictionary by value

my_dicc = {"Hola": "Adiós", "MiCasa": "TuCapa", "Quien": "puma", 20:"voy"}
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print(sorted(d.items(), key=(lambda x : x[1])))
print(sorted(d.items(), key=(lambda x : x[1]), reverse=True))