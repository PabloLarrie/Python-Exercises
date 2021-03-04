# Write a Python program to compute the future value of a specified
# principal amount, rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79


def intereses(amt, int, years):
    dinero = amt
    intereses = int / 100 + 1
    for amt in range(years):
        dinero = dinero * intereses
    return dinero


print(intereses(10000, 3.5, 7))
print(intereses(0.93, 2.25, 1000))  # Dinero que gana Fry en Futurama xDD
