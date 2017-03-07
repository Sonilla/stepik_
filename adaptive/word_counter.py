"""
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве
используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова,
разделённые пробелом и вывести получившуюся статистику.
Программа должна выводить для каждого уникального слова число его повторений (без учёта регистра).
Формат ввода:
Одна строка, содержащая последовательности символов через пробел
Формат вывода:
Набор строк, каждая из которых содержит слово и, через пробел, число −− количество раз, которое слово использовалось во входной строке. Регистр слов не важен, слова в выводе не должны повторяться, порядок слов произвольный.
"""
lst = input().lower().split()
uniq = set(lst)
d = {}
for s in uniq:
    d[s] = lst.count(s)

for i in d:
    print(i,d[i])

'''
d = {}
for i in input().lower().split():
    d.setdefault(i, 0)
    d[i] += 1
for k,v in d.items():
    print(k,v)
    '''