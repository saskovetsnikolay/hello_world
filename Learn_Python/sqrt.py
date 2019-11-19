from math import sqrt
def sqrt1(a, b, c):
    sqrt2 = b + (sqrt((b ** 2) + 4 *a *c))
    sqrt2 /= 2 *a
    sqrt2 -= (a ** 3) * c + (b ** -2)
    return sqrt2
print(sqrt1(1, 2, 3))
