"""6. Радиус окружности 5 с центром в начале координат. Определить лежит ли точка с координатами введенными пользователем посредством input в данной окружности.  """

def point_in_circle(a, b):
    r = 5
    ax = 0
    bx = 0
    a = (a - ax) ** 2 + (b - bx) ** 2
    return a < r ** 2

a = int(input())
b = int(input())
print(point_in_circle(a, b)) 
