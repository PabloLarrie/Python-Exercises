# Write a Python program to remove and print every third 
# number from a list of numbers until the list becomes empty.
import itertools


listaa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# for values in range(len(listaa)): 
#     f = 1
#     for i, v in enumerate(listaa):
#         if i == 3 * f - f:
#             print(v)
#             listaa.pop(i)
#             f += 1
#     if len(listaa) <= 2:
#         for v in range(len(listaa)):
#             listaa.pop(len(listaa) - 1)            #me cago en tó! putos ejercicios mal explicados

# print(listaa)


def dele(listt):
    leng = len(listt)
    ind = 0
    while leng > 0:
        ind = (2 + ind) % leng
        print(listt.pop(ind))
        leng -= 1
    
dele(listaa)
print(listaa)
