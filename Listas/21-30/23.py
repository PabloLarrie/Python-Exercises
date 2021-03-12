# Write a Python program to flatten a shallow list.

shallow_list = [2, [1, 0], [3, 1], [[2, 4], 5]]

# recursive / recursividad


def shallowed(listed):
    result = []
    for v in listed:
        if type(v) == int:
            result.append(v)
        elif type(v) == list:
            result += shallowed(v)

    return result


print(shallowed(shallow_list))
