def div(*args):

    try:
        numb_1 = int(input('Введите число которе делим: '))
        numb_2 = int(input('Введите число на которое будем делить: '))
        res = numb_1 / numb_2
    except ValueError:
        return 'Ошибка ввода'
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

    return res

print(f'Результат деления: {div()}')
