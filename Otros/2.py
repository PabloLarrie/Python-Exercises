arr = [2,3,6,6,5]
ms = sorted(arr, reverse=True)

total = 0    
for v in arr:    
    if v < ms[0]:
        total = v
    
print(ms)
print(total)