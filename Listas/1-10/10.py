# Write a Python program to find the list of words that are 
# longer than n from a given list of words. Go to the editor.

sample_list = ['abc', 'xyz', 'aba', '1221', 'caac', 'moso', 'tronco', 'oso', 'huesoh', 'aa']

longitude = int(input("intruduce el tamaño de la lista :"))

list_words = []
for value in sample_list:
    if len(value) > longitude:
        list_words.append(value)

print(list_words)
