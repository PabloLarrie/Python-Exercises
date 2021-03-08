# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

k = input("Introduce el número: ")
g = k + k
i = g + k
final = int(k) + int(k + k) + int(k + k + k)
print(final)
