'''
max и min
Дано натуральное число n, \, (n \ge 10)n,(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести максимальную и минимальную цифры введенного числа (с поясняющей надписью).
'''
n = int(input())
max_digit = n % 10
min_digit = n % 10
while n != 0:
    last_digit = n % 10
    if last_digit > max_digit:
        max_digit = last_digit
    if last_digit < min_digit:
        min_digit = last_digit
    n //= 10
print(f"Максимальная цифра равна {max_digit}")
print(f"Минимальная цифра равна {min_digit}")
