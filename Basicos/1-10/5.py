# Write a Python program which accepts the user's first and last name 
# and print them in reverse order with a space between them.

print(' '.join(reversed(input("first and last name:\n").split(' '))))
