# Write a Python function that takes a sequence of numbers and 
# determines whether all the numbers are different from each other.

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sq = set(sequence)

if sequence == list(sq):
    print(True)
else:
    print(False)