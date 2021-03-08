def is_leap(year):
    leap = True
    if year % 400 == 0:
        print("1")
        return leap
    elif year % 100 == 0:
        print("2")
        leap = False
        return leap
    elif year % 4 == 0:
        print("3")
        return leap
    else:
        print("4")
        leap = False
        return leap  

year = int(input())
print(is_leap(year))