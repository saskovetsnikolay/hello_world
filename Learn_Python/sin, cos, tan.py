from math import cos, sin, tan
def cst(x, y):
    a = sin(x) + cos(y)
    a /= cos(x) - sin(y)
    a *= tan(x*y)
    return a
print(cst(1, 2))