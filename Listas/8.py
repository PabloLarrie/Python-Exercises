# Write a Python program to check a list is empty or not

sample_list = ['abc', 'xyz', 'aba', '1221', 'caac', 'moso', 'tronco', 'oso', 'huesoh', 'aa', 'xyz', 'caac']
empty_list = []

def emptyness (listt):
    if listt == []:
        print("La lista está vacia")
    else:
        print("La lista no está vacia")

emptyness(sample_list)
emptyness(empty_list)