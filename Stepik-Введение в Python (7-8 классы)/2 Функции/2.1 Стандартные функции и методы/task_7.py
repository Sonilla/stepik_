'''
Два максимума
    Числа вводятся с клавиатуры через запятую. Выведите два самых больших по модулю чисел ряда. Числа выведите по неубыванию абсолютного значения через пробел. Гарантируется, что в наборе чисел есть как минимум два уникальных числа, а также то, что искомые два максимума не равны друг другу по модулю.
'''

arr = [int(i) for i in input().replace(' ', '').split(',')]

arr.sort(key=abs)
print(arr[-2], arr[-1])
