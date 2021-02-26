# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

programa = input("Introduzca aquí su programa :")
posicion = programa.find('.') + 1

print(programa[posicion:])