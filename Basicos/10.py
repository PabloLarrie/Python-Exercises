# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

value = input("Introduce el número: ")
k = str(value)
g = k + k
i = g + k
final = int(k) + int(g) + int(i)
print(final)
