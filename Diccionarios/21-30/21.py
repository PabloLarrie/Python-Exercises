# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# data = {"1": ["a", "b"], "2": ["c", "d"]}
# Expected Output:
# ac
# ad
# bc
# bd
data = [
    ["a", "b", "a"],
    ["c", "d"],
    ["c", "a", "c"],
]

result = []
n = len(data)  # 3
sizes = [len(d) for d in data]  # [2, 2, 3]
indexes = [0] * n  # [0, 0, 0]
multiply = 1
for v in data:
    multiply *= len(v)

f = [v for v in range(n)]
while True:
    minilista = []
    for x, y in zip(f, indexes):
        minilista.append(data[x][y])
    result.append(minilista)
    print(minilista)
    for i in range(len(indexes) - 1, -1, -1):
        if indexes[i] + 1 < sizes[i]:
            indexes[i] += 1
            break
        else:
            indexes[i] = 0
    if len(result) == multiply:
        break
