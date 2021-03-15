# Write a Python program to create the combinations of 3 digit combo.
import itertools

litt = [3, 5, 7]



def bouclezer(lista):
    vueltas = 0
    litts = []
    ruedas = 0
    for _ in range(6):
        lit = []
        for i, v in enumerate(lista):
            if len(lit) == 0 and i >= vueltas:
                lit.append(v)
                for j, h in enumerate(lista):
                    if len(lit) == 1 and h not in lit and j >= ruedas:
                        lit.append(h)
                        ruedas += 1/2
                        for b in (lista):
                            if len(lit) == 2 and b not in lit:
                                lit.append(b)
        vueltas += 1.25
        if len(lit) == 3:
            litts.append(lit)
    return litts


print(bouclezer(litt))
print(list(itertools.permutations(litt)))
