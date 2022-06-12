'''
Кэширование
    Оптимизируйте рекурсивный алгоритм вычисления чисел Фибоначчи из лекции таким образом, чтобы функция не делала лишних вычислений, то есть запоминала бы уже вычисленные значения. Кроме функции fib(n) ничего писать не нужно, однако вне функции Вы можете объявить нужные Вам глобальные переменные. Известно, что n <= 650.
'''
d = {0: 1, 1: 1, 2: 1}


def fib(n):
    if n in d:
        return d.get(n)
    else:
        d[n - 2] = fib(n - 2)
        d[n - 1] = fib(n - 1)
        return d[n - 2] + d[n - 1]


# n = int(input())
print(fib(42))
print(d)
