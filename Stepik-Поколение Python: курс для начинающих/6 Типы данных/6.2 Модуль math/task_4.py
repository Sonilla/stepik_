'''
Тригонометрическое выражение
Напишите программу, вычисляющую значение тригонометрического выражения
 по заданному числу градусов x.

Формат входных данных
На вход программе подается одно вещественное число xx измеряемое в градусах.

Формат выходных данных
Программа должна вывести одно число – значение тригонометрического выражения.
'''

from math import *

x = float(input())
r = radians(x)
s = sin(r) + cos(r) + tan(r)**2

print(s)

