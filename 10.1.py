def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """

    for el in range(end):

     yield begin
     begin = func(begin)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True
assert list(gen) == [2, 4, 16, 256]
print('OK')