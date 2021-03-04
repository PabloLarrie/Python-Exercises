#  Write a Python program to get the difference between a given number and 17,
#  if the number is greater than 17 return double the absolute difference

given = int(input("number :"))

count = given - 17

if given > 17:
    count = count * 2

print(abs(count))


def difference(n):
    result = n - 17
    if n > 17:
        result = result * 2
        return result
    else:
        return abs(result)


print(difference(22))
print(difference(14))