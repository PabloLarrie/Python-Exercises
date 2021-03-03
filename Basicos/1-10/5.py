# Write a Python program which accepts the user's first and last name 
# and print them in reverse order with a space between them.

personal_data = input("Introduce here your name and surname :")
data_sentence = personal_data.split(' ')
reversed_sentence = ' '.join(reversed(data_sentence))

print((reversed_sentence))
