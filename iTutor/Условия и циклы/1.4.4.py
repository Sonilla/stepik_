'''
В данной задаче необходимо найти и вывести произведение всех цифр числа, за исключением 0.

Примечание: Используйте особенности конвертации типов данных и циклы, конечно же!

Формат входных данных: Натуральное число

Формат выходных данных: Натуральное число


Sample Input:

1203450
Sample Output:

120
'''

lst = []

n = int(input())
while True:
    m = n % 10
    if m != 0:
        lst.append(m)
    n = n // 10
    if n == 0: break

sum = 1
for i in lst:
    sum *= i

print(sum)
