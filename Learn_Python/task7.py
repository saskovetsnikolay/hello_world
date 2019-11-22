"""Даны два угла треугольника (в градусах). Определить, существует ли такой треугольник, и если да, то будет ли
он прямоугольным."""

def triangle(a, b):
    c = 180
    d = 180 - (a +b)
    if (a + b) < c:
        print("Triangle exists.")
        if a == 90 or b == 90 or d == 90:
            print("Triangle's rectangular.")
        else:
            print("Triangle don't rectangular.")    
    else:
        print("Triangle don't exist.")

a = float(input())
b = float(input())
triangle(a, b)