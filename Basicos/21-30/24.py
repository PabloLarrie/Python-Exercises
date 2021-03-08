# Write a Python program to test whether a passed letter is a vowel or not.

vowel = ["a", "e", "i", "o", "u"]


def vowelizer(l):
    if l.casefold() in vowel:
        return "Es una vocal"
    return "No es una vocal"


print(vowelizer("I"))
print(vowelizer("j"))