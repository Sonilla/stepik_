'''
Определить количество
    С клавиатуры вводится ряд чисел через запятую. Определите количество чисел, равных максимуму последовательности.
'''

arr = [int(i) for i in input().replace(' ', '').split(',')]
m = max(arr)
print(arr.count(m))
