"""4. Дано действительное число R вида nnn.ddd (три цифровых разряда в дробной и целой частях). Поменять местами
дробную и целую части числа и вывести полученное значение числа."""

def change_whole_and_fractional_parts(n):
    x = (n * 1000) % 1000 + int(n) /1000
    return x
print(change_whole_and_fractional_parts(122.321)) 