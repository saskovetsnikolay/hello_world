"""4. Дано действительное число R вида nnn.ddd (три цифровых разряда в дробной и целой частях). Поменять местами
дробную и целую части числа и вывести полученное значение числа."""

# n = float(input())
# print((n * 1000) % 1000 + int(n) / 1000)

# s = input().strip()
# print(*s.partition('.')[::-1], sep='')


# from decimal import Decimal
# (d%1)*1000+Decimal(int(d))/1000
# Decimal('210.543')


r = 666.555
print(str(r)[::-1])