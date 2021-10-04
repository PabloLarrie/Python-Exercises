# Write a Python program which accepts a sequence of comma-separated numbers 
# from the user and generates a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

lista = [valor for valor in input("Indique aquí su lista :").replace(' ', '').split(',')]
print(f"List: {lista}\nTuple: {tuple(lista)}")
