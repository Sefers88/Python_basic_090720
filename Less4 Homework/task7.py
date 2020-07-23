from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

numbers = (int(input('Программа расчитывает факториал чисел начиная от 1, введите число до которого вы хотите узнать результаты: ')))

gen = fact()
x = 1
for i in gen:
    if x <= numbers:
        print(f'Факториал от {x} = {i}')
        x += 1
    else:
        break
