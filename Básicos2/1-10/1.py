# Write a Python functifinal_liston that takes a sequence of numbers and
# determines whether all the numbers are different from each other.

sequence = [1, 3, 5, 4, 7, 6, 9, 8, 2, 2, 2, 8]
sequence2 = [1, 2]

if len(sequence) != len(set(sequence)):
    print("Hay números repetidos.")
else:
    print("Todos los elementos son diferentes.")


print(bool(sequence))
print(bool(sequence2))
