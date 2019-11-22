"""5. Дано натуральное число Т, которое представляет длительность прошедшего времени в секундах. Вывести
данное значение длительности в часах, минутах и секундах в следующей форме:
ННч ММмин SSc."""


def seconds_to_string(seconds):
    mm, ss = divmod(seconds, 60)
    hh, mm = divmod(mm, 60)
    return "%02d:%02d:%02d" % (hh, mm, ss)
s = int(input())
print(seconds_to_string(s))
