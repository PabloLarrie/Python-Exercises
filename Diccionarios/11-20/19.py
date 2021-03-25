# Write a Python program to combine two dictionary adding values for common keys.
from collections import Counter

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
d3 = {"a": 5, "e": 200}

print(Counter(d1) + Counter(d2))


def suma_dicts(param1, param2):
    return {
        k: param1.get(k, 0) + param2.get(k, 0) for k in param1.keys() | param2.keys()
    }


def suma_dicts2(param1, param2):
    result = param1.copy()
    for k, v in param2.items():
        if k in result:
            result[k] += v
        else:
            result[k] = v
    return result


print(suma_dicts(d1, d2))


class SumaNumeros:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        """
        Se ejecuta cuando sumas un SumaNumeros con otra cosa
        """
        return SumaNumeros(self.a + other.a, self.b + other.b)

    def __eq__(self, other):
        """
        Se ejecuta  cuando comparas un SumaNumeros con otra cosa
        """
        return self.a == other.a and self.b == other.b

    def __str__(self):
        """
        Se ejecuta  cuando se intenta transformar una instancia de SumaNumeros con otra cosa
        """
        return f"a: {str(self.a)}, b: {str(self.b)}"


n1 = SumaNumeros(2, 5)
n2 = SumaNumeros(2, 9)
final = n1 + n2

print(final.a, final.b)
print(n1 == n1)
print(n1 == n2)
print(final)
