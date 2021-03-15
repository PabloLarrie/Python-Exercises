# Write a Python program to find unique triplets whose three 
# elements gives the sum of zero from an array of n integers

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, -3, 12, -2, 5, 6, 18, 0, 10, 0]

# triplet_of_triplets = []
# vueltas = 0

# for _ in liste:
#     triplets = []
#     for i, v in enumerate(liste):
#         if len(triplets) < 1 and i >= vueltas:
#             triplets.append(v)
#         if len(triplets) < 2 and sum(triplets, v) == 10:
#             triplets.append(v)
        
#     if len(triplets) == 2:
#         triplet_of_triplets.append(triplets)
#     vueltas += 1

# print(triplet_of_triplets)
# while sum(triplets) != 10:
#     if liste:

triplet_of_triplets = []
vueltas = 0

for _ in liste:
    triplets = []
    for i, v in enumerate(liste):
        if len(triplets) < 1 and i >= vueltas:
            triplets.append(v)
        elif len(triplets) == 1 and v not in triplets:
            triplets.append(v)
        elif len(triplets) == 2 and sum(triplets, v) == 10:
            triplets.append(v)
        
    if len(triplets) == 3:
        triplet_of_triplets.append(triplets)
    vueltas += 1

print(triplet_of_triplets)


