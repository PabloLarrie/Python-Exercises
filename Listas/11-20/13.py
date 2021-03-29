# Write a Python program to generate a 3*4*6 3D array whose each element is *.
# Básicamente es un array de 3 dimensiones que representa un cubo de 3 * 4 * 6 caras.
# Por ejemplo, un cuadrado de 2 dimensiones de 2 * 4 sería [[1, 2], [3, 4], [5, 6], [7, 8]].

cube = []

for v in range(6):
    main = []
    for g in range(3):
        basic = []
        for d in range(4):
            basic.append(d)
        main.append(basic)
    cube.append(main)

for v in cube:
    print(v)

# print(cube)

cube2 = [[["uwu" for _ in range(4)] for _ in range(3)] for _ in range(6)]

for v in cube2:
    print(v)