# Write a Python program to count the number of strings where the 
# string length is 2 or more and the first and last character are the same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

sample_list = ['abc', 'xyz', 'aba', '1221', 'caac', 'moso', 'tronco', 'oso', 'huesoh', 'aa']

count = 0
for v in sample_list:
    if len(v) > 2 and v[0] == v[-1]:
        count += 1

print (count)